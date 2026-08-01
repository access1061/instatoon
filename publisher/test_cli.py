import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from publisher.cli import InstagramPublisher, Media, ThreadsPublisher, fingerprint, github_media, load_env


class PublisherTests(unittest.TestCase):
    def test_load_env_does_not_overwrite_existing_secret(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / ".env"
            path.write_text("TOKEN=file-value\n", encoding="utf-8")
            with patch.dict(os.environ, {"TOKEN": "process-value"}, clear=False):
                load_env(path)
                self.assertEqual(os.environ["TOKEN"], "process-value")

    def test_fingerprint_changes_with_caption(self):
        with tempfile.TemporaryDirectory() as directory:
            image = Path(directory) / "a.png"
            image.write_bytes(b"png")
            self.assertNotEqual(fingerprint([image], "one", "thread"), fingerprint([image], "two", "thread"))

    def test_instagram_carousel_flow(self):
        publisher = InstagramPublisher("v1", "123", "token")
        publisher.client.request = Mock(side_effect=[{"id": "c1"}, {"id": "c2"}, {"id": "parent"}, {"id": "post"}])
        post_id = publisher.publish([Media(Path("1.png"), "https://x/1.png"), Media(Path("2.png"), "https://x/2.png")], "caption")
        self.assertEqual(post_id, "post")
        self.assertEqual(publisher.client.request.call_count, 4)

    def test_threads_text_flow(self):
        publisher = ThreadsPublisher("v1", "me", "token")
        publisher.client.request = Mock(side_effect=[{"id": "container"}, {"id": "post"}])
        self.assertEqual(publisher.publish([], "hello"), "post")

    @patch("publisher.cli.requests.get")
    def test_github_media_uses_repo_relative_path(self, get):
        response = Mock(status_code=200)
        get.return_value = response
        with patch.dict(os.environ, {"GITHUB_RAW_BASE_URL": "https://raw.example/main"}, clear=False):
            media = github_media([Path(__file__).resolve()])
        self.assertTrue(media[0].url.endswith("publisher/test_cli.py"))
        response.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
