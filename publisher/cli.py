from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import sqlite3
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import quote

import requests


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "publisher" / "data"
DB_PATH = DATA_DIR / "publish-history.sqlite3"


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def require_env(*names: str) -> dict[str, str]:
    values = {name: os.getenv(name, "").strip() for name in names}
    missing = [name for name, value in values.items() if not value]
    if missing:
        raise RuntimeError("Missing environment variables: " + ", ".join(missing))
    return values


@dataclass(frozen=True)
class Media:
    path: Path
    url: str


class ApiError(RuntimeError):
    pass


class MetaClient:
    def __init__(self, token: str, timeout: int = 60):
        self.token = token
        self.timeout = timeout

    def request(self, method: str, url: str, **kwargs) -> dict:
        headers = dict(kwargs.pop("headers", {}))
        headers["Authorization"] = f"Bearer {self.token}"
        response = requests.request(method, url, headers=headers, timeout=self.timeout, **kwargs)
        try:
            body = response.json()
        except ValueError:
            body = {"raw": response.text[:1000]}
        if not response.ok or "error" in body:
            raise ApiError(f"Meta API {response.status_code}: {json.dumps(body, ensure_ascii=False)}")
        return body


class InstagramPublisher:
    def __init__(self, api_version: str, user_id: str, token: str):
        self.base = f"https://graph.instagram.com/{api_version}/{user_id}"
        self.client = MetaClient(token)

    def publish(self, media: list[Media], caption: str) -> str:
        if not media:
            raise ValueError("Instagram requires at least one image")
        if len(media) == 1:
            container = self.client.request("POST", f"{self.base}/media", data={
                "image_url": media[0].url, "caption": caption,
            })["id"]
        else:
            children = []
            for item in media:
                child = self.client.request("POST", f"{self.base}/media", data={
                    "image_url": item.url, "is_carousel_item": "true",
                })["id"]
                children.append(child)
            container = self.client.request("POST", f"{self.base}/media", data={
                "media_type": "CAROUSEL", "children": ",".join(children), "caption": caption,
            })["id"]
        return self.client.request("POST", f"{self.base}/media_publish", data={
            "creation_id": container,
        })["id"]


class ThreadsPublisher:
    def __init__(self, api_version: str, user_id: str, token: str):
        self.base = f"https://graph.threads.net/{api_version}/{user_id}"
        self.client = MetaClient(token)

    def publish(self, media: list[Media], text: str) -> str:
        if not media:
            container = self.client.request("POST", f"{self.base}/threads", data={
                "media_type": "TEXT", "text": text,
            })["id"]
        elif len(media) == 1:
            container = self.client.request("POST", f"{self.base}/threads", data={
                "media_type": "IMAGE", "image_url": media[0].url, "text": text,
            })["id"]
        else:
            children = []
            for item in media:
                child = self.client.request("POST", f"{self.base}/threads", data={
                    "media_type": "IMAGE", "image_url": item.url, "is_carousel_item": "true",
                })["id"]
                children.append(child)
            container = self.client.request("POST", f"{self.base}/threads", data={
                "media_type": "CAROUSEL", "children": ",".join(children), "text": text,
            })["id"]
        return self.client.request("POST", f"{self.base}/threads_publish", data={
            "creation_id": container,
        })["id"]


def github_media(paths: Iterable[Path]) -> list[Media]:
    cfg = require_env("GITHUB_RAW_BASE_URL")
    result = []
    for path in paths:
        try:
            relative = path.relative_to(ROOT).as_posix()
        except ValueError as exc:
            raise RuntimeError(f"GitHub media must be inside the repository: {path}") from exc
        url = cfg["GITHUB_RAW_BASE_URL"].rstrip("/") + "/" + quote(relative, safe="/")
        response = requests.get(url, timeout=30, stream=True)
        response.close()
        if response.status_code != 200:
            raise RuntimeError(
                f"Media is not publicly available ({response.status_code}): {url}. "
                "Commit and push the image to the configured branch first."
            )
        result.append(Media(path=path, url=url))
    return result


def s3_media(paths: Iterable[Path]) -> list[Media]:
    try:
        import boto3
    except ImportError as exc:
        raise RuntimeError("S3 media mode requires: python -m pip install boto3") from exc
    cfg = require_env("MEDIA_BUCKET", "MEDIA_PUBLIC_BASE_URL", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY")
    endpoint = os.getenv("S3_ENDPOINT_URL") or None
    region = os.getenv("AWS_DEFAULT_REGION", "auto")
    client = boto3.client("s3", endpoint_url=endpoint, region_name=region)
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    result = []
    for path in paths:
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        key = f"insta-toon/{day}/{uuid.uuid4().hex}-{path.name}"
        client.upload_file(str(path), cfg["MEDIA_BUCKET"], key, ExtraArgs={"ContentType": content_type})
        url = cfg["MEDIA_PUBLIC_BASE_URL"].rstrip("/") + "/" + quote(key, safe="/")
        result.append(Media(path=path, url=url))
    return result


def prepare_media(paths: Iterable[Path]) -> list[Media]:
    provider = os.getenv("MEDIA_PROVIDER", "github").strip().lower()
    if provider == "github":
        return github_media(paths)
    if provider == "s3":
        return s3_media(paths)
    raise RuntimeError("MEDIA_PROVIDER must be 'github' or 's3'")


def fingerprint(paths: list[Path], instagram_caption: str, threads_text: str) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.read_bytes())
    digest.update(instagram_caption.encode())
    digest.update(threads_text.encode())
    return digest.hexdigest()


def connect_db() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.execute("""CREATE TABLE IF NOT EXISTS publications (
        fingerprint TEXT NOT NULL, platform TEXT NOT NULL, status TEXT NOT NULL,
        post_id TEXT, error TEXT, created_at TEXT NOT NULL,
        UNIQUE(fingerprint, platform)
    )""")
    return db


def record(db: sqlite3.Connection, fp: str, platform: str, status: str, post_id: str | None = None,
           error: str | None = None) -> None:
    db.execute("""INSERT INTO publications(fingerprint, platform, status, post_id, error, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(fingerprint, platform) DO UPDATE SET
        status=excluded.status, post_id=excluded.post_id, error=excluded.error,
        created_at=excluded.created_at""",
        (fp, platform, status, post_id, error, datetime.now(timezone.utc).isoformat()))
    db.commit()


def already_published(db: sqlite3.Connection, fp: str, platform: str) -> bool:
    row = db.execute("SELECT status FROM publications WHERE fingerprint=? AND platform=?", (fp, platform)).fetchone()
    return bool(row and row[0] == "published")


def read_text(value: str | None, file: str | None) -> str:
    if file:
        return Path(file).resolve().read_text(encoding="utf-8").strip()
    return (value or "").strip()


def validate_config(platform: str) -> None:
    require_env("META_API_VERSION")
    provider = os.getenv("MEDIA_PROVIDER", "github").strip().lower()
    if provider == "github":
        require_env("GITHUB_RAW_BASE_URL")
    elif provider == "s3":
        require_env("MEDIA_BUCKET", "MEDIA_PUBLIC_BASE_URL", "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY")
    else:
        raise RuntimeError("MEDIA_PROVIDER must be 'github' or 's3'")
    if platform in ("instagram", "both"):
        require_env("INSTAGRAM_USER_ID", "INSTAGRAM_ACCESS_TOKEN")
    if platform in ("threads", "both"):
        require_env("THREADS_USER_ID", "THREADS_ACCESS_TOKEN")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Publish approved Insta Toon assets to Meta platforms")
    parser.add_argument("--env-file", default=str(ROOT / ".env"))
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("validate", help="Check required configuration without publishing")
    check.add_argument("--platform", choices=("instagram", "threads", "both"), default="both")
    publish = sub.add_parser("publish", help="Upload media and publish after explicit approval")
    publish.add_argument("--platform", choices=("instagram", "threads", "both"), default="both")
    publish.add_argument("--images", nargs="+", required=True)
    publish.add_argument("--instagram-caption")
    publish.add_argument("--instagram-caption-file")
    publish.add_argument("--threads-text")
    publish.add_argument("--threads-text-file")
    publish.add_argument("--confirm", action="store_true", help="Required explicit publication approval")
    publish.add_argument("--force", action="store_true", help="Allow intentional duplicate publishing")
    args = parser.parse_args(argv)
    load_env(Path(args.env_file))
    if args.command == "validate":
        validate_config(args.platform)
        print("Configuration is complete.")
        return 0
    if not args.confirm:
        parser.error("Publishing requires --confirm (the user's explicit approval).")
    validate_config(args.platform)
    paths = [Path(item).resolve() for item in args.images]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing image files: " + ", ".join(missing))
    ig_caption = read_text(args.instagram_caption, args.instagram_caption_file)
    threads_text = read_text(args.threads_text, args.threads_text_file)
    fp = fingerprint(paths, ig_caption, threads_text)
    db = connect_db()
    platforms = [args.platform] if args.platform != "both" else ["instagram", "threads"]
    pending = [p for p in platforms if args.force or not already_published(db, fp, p)]
    if not pending:
        print("Skipped: this exact content has already been published to the requested platforms.")
        return 0
    media = prepare_media(paths)
    version = os.environ["META_API_VERSION"]
    results = {}
    for platform in pending:
        try:
            if platform == "instagram":
                post_id = InstagramPublisher(version, os.environ["INSTAGRAM_USER_ID"], os.environ["INSTAGRAM_ACCESS_TOKEN"]).publish(media, ig_caption)
            else:
                post_id = ThreadsPublisher(version, os.environ["THREADS_USER_ID"], os.environ["THREADS_ACCESS_TOKEN"]).publish(media, threads_text)
            record(db, fp, platform, "published", post_id=post_id)
            results[platform] = {"status": "published", "post_id": post_id}
        except Exception as exc:
            record(db, fp, platform, "failed", error=str(exc))
            results[platform] = {"status": "failed", "error": str(exc)}
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 1 if any(item["status"] == "failed" for item in results.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
