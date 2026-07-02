# Insta Toon Codex Workspace

한국어 원고를 분석해 손그림 본문 삽화와 인스타툰 스타일 이미지를 만들기 위한 Codex 작업 폴더입니다.

이 환경은 `https://github.com/access1061/codex_illu_making.git`의 스킬 구성을 참고해 현재 폴더용으로 정리했습니다.

## 폴더 구조

```text
.
├─ AGENTS.md
├─ README.md
├─ assets/
│  └─ YYYY-MM-DD/
├─ scripts/
│  └─ install-skills.ps1
└─ skills/
   ├─ handdrawn-illustrations/
   ├─ handdrawn-illustrations2/
   └─ handdrawn-illustrations3/
```

## 권장 사용

현재 주력 스킬은 `skills/handdrawn-illustrations3`입니다.

```text
아래 원고를 인스타툰으로 작성해줘.

[원고]
```

사용자가 장수나 루프를 직접 지정하지 않아도 Codex가 원고 규모를 판단합니다.

- 1장 단편으로 충분하면 바로 생성할지, Forge 루프로 shot list부터 잡을지 묻습니다.
- 2장 이상이 자연스럽거나 정보량이 큰 원고는 자동으로 Forge 루프를 적용합니다.
- 기본 루프는 `Ask/Plan -> Run -> Verify -> Learn -> Done`입니다.
- 한글 말풍선과 텍스트 오버레이는 gpt image-gen 생성 단계에서 직접 넣습니다.

## 스킬 설치

Codex 전역 스킬로 등록하려면 PowerShell에서 다음을 실행합니다.

```powershell
.\scripts\install-skills.ps1
```

설치 대상:

```text
$env:USERPROFILE\.codex\skills\
```

이미 같은 이름의 스킬이 있으면 덮어씁니다.

## 결과 저장

생성된 이미지는 현재 폴더의 날짜별 자산 폴더에 저장합니다.

```text
assets/YYYY-MM-DD/
```

예:

```text
assets/2026-07-02/01-core-idea.png
```

같은 파일명이 있으면 `-v2`, `-v3`처럼 버전을 붙여 기존 결과물을 보존합니다.

## 검증

스킬 메타데이터 검증 스크립트가 설치되어 있다면 다음을 실행할 수 있습니다.

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skills\handdrawn-illustrations
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skills\handdrawn-illustrations2
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skills\handdrawn-illustrations3
```
