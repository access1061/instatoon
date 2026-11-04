# Insta Toon Agent Team

## 시작

프로젝트 전용 CLI: `scripts/paseo.ps1`. 팀: `.agents/teams/instatoon.json`.

설치된 로컬 웹 UI는 http://127.0.0.1:6799 이다. 릴레이는 비활성화되어 있다. CLI 래퍼는 기본적으로 프로젝트의 `.paseo-local` 데몬을 사용하며 설치 파일과 런타임 상태는 Git에서 제외한다.

다른 PC에서 저장소를 복제하면 런타임도 설치해야 한다:

```powershell
npm.cmd install --prefix .tools/paseo @getpaseo/cli@0.15.0 --no-audit --no-fund
.\scripts\paseo.ps1 daemon config set daemon.listen 127.0.0.1:6799
.\scripts\paseo.ps1 daemon config set daemon.relay.enabled false
.\scripts\paseo.ps1 daemon config set features.webUi.enabled true
.\scripts\paseo.ps1 daemon config set pluginsEnabled true
.\scripts\paseo.ps1 daemon start --timeout 45
.\scripts\paseo.ps1 plugin add gyuha/agent-team
.\scripts\paseo.ps1 project create
.\scripts\paseo.ps1 workspace create --isolation local --path . --title instatoon
```

이후 재시작은 `.\scripts\paseo.ps1 daemon start`, 종료는 `.\scripts\paseo.ps1 daemon stop`을 사용한다. 설치 검증은 CLI 0.15.0, 웹 UI HTTP 200, 플러그인 running, Codex available, gpt-6.1-sol 목록 확인까지 수행했다. 팀 Apply와 실제 원고 생성·QA는 별도 실행 단계이며 이미지 생성 도구 연결은 아직 검증하지 않았다.

```powershell
.\scripts\paseo.ps1 --version
.\scripts\paseo.ps1 provider ls
.\scripts\paseo.ps1 provider models codex
```

기본 provider/model은 codex/gpt-6.1-sol이다. 호스트에서 사용 가능해야 한다. 불가능하면 임의 대체하지 말고 팀 패널에서 실제 모델을 선택한다. Paseo에서 이 프로젝트와 `instatoon` 워크스페이스를 열고 Agent teams에서 기존 팀 파일을 확인하고 Apply한다. JSON만으로 팀이 자동 시작되지는 않는다. workspace 제목은 팀의 orchestrator.workspace와 일치해야 한다.

## 총괄 실행 순서

1. AGENTS.md와 선택한 스킬을 읽고 사용자 지시를 우선한다. 작업 ID `<날짜>-<topic>`를 정하며 기존 작업이 있으면 -v2 등을 붙인다.
2. `docs/jobs/<job-id>/request.md`에 원고, 출처, 장수, 스타일, 정확한 문구, 실제 참고 경로와 참조 범위를 저장한다. 원본은 보존한다.
3. editor에 Read/Plan을 위임한다. `plan.md`에 장 역할/핵심 의미/캐릭터 행동/정확한 문구를 기록한다. 기획 요청이 아니면 중간 기획 승인을 요구하지 않는다.
4. artist에게 한 장의 기획·참고·출력 경로를 전달한다. 생성과 편집 도구가 실제로 있는지 먼저 확인한다. 없으면 BLOCKED_TOOL로 보고한다. 프롬프트 작성만으로 이미지 생성 완료가 아니다.
5. visual-qa에 원고·기획·참고 이미지·앵커·검수 대상 경로를 전달한다. 실제 이미지를 열어 비교한 보고서를 받는다.
6. REVISE이면 artist에 위치/문제/수정/유지 지시를 전달해 새 버전을 만들고 재검수한다. 기본 수정 한도는 장당 2회다. 계속 실패하면 미완료로 전달한다. 사용자 지정 문구를 임의 축약하지 않는다.
7. 첫 장 PASS 후 실제 파일을 앵커로 고정해 후속 장에도 입력한다. 제작과 검수를 한 장씩 순서대로 진행한다. 같은 파일에 동시 쓰기하지 않는다.
8. 이미지가 완료되면 editor가 `caption.md`를 작성한다. 총괄이 공백 포함 100~500자를 확인하고 최종 캡션을 날짜 폴더에 복사한다.
9. 인스타 최종 이미지는 기존 보정기로 별도 파일에 저장하고 실제 1080×1350인지 검사한다. QA에게 최종본의 여백·글자 크기·가독성도 확인시킨다. 비인스타/명시 비율은 사용자 지시를 따른다.
10. `result.md`에 최종 이미지·캡션·앵커·QA 경로와 미해결 항목을 기록하고 전달한다. QA 통과는 Git 공개나 게시 승인이 아니다.

```powershell
python skills/handdrawn-illustrations3/scripts/fit_instagram_4x5.py assets/YYYY-MM-DD/raw/01-topic.png assets/YYYY-MM-DD/01-topic.png
```

## 파일 소유권

| 담당 | 쓰기 범위 |
| --- | --- |
| 총괄 | request.md, result.md, 최종 이미지와 최종 캡션 |
| editor | 해당 작업의 plan.md, caption.md |
| artist | 할당된 assets 날짜 폴더의 raw/ 이미지와 prompts/ 프롬프트 |
| visual-qa | 해당 작업의 qa-장번호-버전.md |

폴더 지정은 보안 격리가 아니다. 공유 체크아웃에서 다른 작업자의 변경을 되돌리지 않는다. 각 역할은 추가 에이전트를 시작하지 않는다. 파일은 덮어쓰지 않고 버전 접미사를 붙인다.

## QA 보고서

```text
판정: PASS / REVISE / BLOCKED_TOOL
검수 대상 경로:
실제로 열어 본 참고 이미지 경로:
스타일 앵커 경로:
위치 / 문제 / 수정 지시 / 유지할 요소:
미확인 사항:
```

선택한 스킬의 QA 기준을 따른다. 판타지 스타일이면 `skills/fantasy-party-insta-toon/references/qa-checklist.md`를 사용한다. 다른 스타일에 판타지 캐릭터를 강제하지 않는다. 이미지 열람 불가나 독립 역할 미실행 상태를 QA 완료로 처리하지 않는다.

## 이미지 도구와 발행

`image_gen`은 이 플러그인에 포함되지 않는다. 제작 역할의 실제 도구 목록에서 확인한다. 없으면 프롬프트와 실제 참고 경로를 생성 가능한 세션에 전달하고 이미지 파일이 저장된 뒤 QA를 재개한다. 기존 이미지 검수는 생성 도구 없이도 이미지 열람 도구가 있으면 가능하다.

`publisher.cli publish --confirm`은 사용자의 명시적 발행 요청이 있을 때만 실행한다. `.env`와 토큰은 팀 설정·프롬프트·보고서에 복사하지 않는다.

## 출처

- https://github.com/gyuha/paseo-agent-team
- https://paseo.sh/plugins/gyuha/agent-team
- https://paseo.sh/docs/cli
