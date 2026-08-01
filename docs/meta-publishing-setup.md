# Instagram + Threads 승인 후 자동 발행 설정

이 도구는 이미지와 원고를 만든 뒤 사용자가 명시적으로 발행을 요청했을 때만 실행한다. CLI의 `--confirm`이 승인 신호이며, 동일 콘텐츠의 중복 게시를 기본적으로 차단한다.

## 1. Meta Developer 앱

Meta Developer Dashboard에서 Business 유형 앱을 만들고 다음 제품을 추가한다.

- Instagram API with Instagram Login
- Threads API

Instagram OAuth 권한:

- `instagram_business_basic`
- `instagram_business_content_publish`

Threads OAuth 권한:

- `threads_basic`
- `threads_content_publish`

본인 계정만 사용하는 초기 단계에서는 앱 관리자/개발자/테스터로 계정을 등록하고 개발 모드에서 테스트할 수 있다. 다른 사용자의 계정을 연결하려면 Live 모드, Advanced Access, App Review와 필요한 비즈니스 인증을 진행한다.

Dashboard에서 Redirect URI를 등록하고 각 제품의 OAuth 흐름으로 토큰을 발급한다. 토큰이나 App Secret은 저장소에 커밋하지 않는다.

## 2. 공개 미디어: GitHub 저장소

Meta 서버는 로컬 파일을 읽을 수 없으므로 HTTPS 공개 URL이 필요하다. 이 저장소는 기본적으로 공개 GitHub raw URL을 사용한다.

```text
https://raw.githubusercontent.com/access1061/instatoon/main/assets/YYYY-MM-DD/image.png
```

따라서 발행 전에 대상 이미지를 이 저장소에 커밋하고 `main` 브랜치로 푸시해야 한다. 게시기는 URL을 직접 조회하여 HTTP 200이 확인되지 않으면 Meta API를 호출하지 않는다. 저장소가 비공개로 바뀌면 이 방식은 작동하지 않는다.

이미지를 GitHub에 공개하고 싶지 않거나 저장소가 비공개라면 `.env.publisher.example`의 S3 설정으로 전환할 수 있다.

## 3. 설치와 검증

```powershell
python -m pip install -r requirements-publisher.txt
Copy-Item .env.publisher.example .env
# .env 값을 입력한 뒤
python -m publisher.cli validate --platform both
python -m unittest publisher.test_cli
```

`META_API_VERSION`은 Meta 앱 Dashboard에 표시된 현재 지원 버전으로 설정한다.

## 4. 승인 후 발행

원고를 UTF-8 텍스트 파일로 저장한 예:

```powershell
python -m publisher.cli publish `
  --platform both `
  --images assets/2026-07-27/01-ai-3d-printing-cover.png assets/2026-07-27/02-ai-code-life-tools.png `
  --instagram-caption-file staging/instagram-caption.txt `
  --threads-text-file staging/threads-text.txt `
  --confirm
```

`--confirm` 없이는 절대 게시하지 않는다. 결과와 오류는 `publisher/data/publish-history.sqlite3`에 기록된다. 같은 이미지와 같은 두 원고는 다시 게시되지 않으며, 정말 중복 게시하려는 경우에만 `--force`를 추가한다.

이미지가 아직 원격 저장소에 없다면 먼저 해당 이미지만 선별하여 커밋·푸시한다. 원고나 `.env`는 공개 저장소에 올리지 않는다.

한 플랫폼이 실패해도 다른 플랫폼의 성공 기록은 유지된다. 동일 명령을 다시 실행하면 이미 성공한 플랫폼은 건너뛰고 실패한 플랫폼만 다시 시도한다.
