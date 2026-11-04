# Insta Toon Agent Team

## 기본 자동 실행 경로

인스타툰 생성 요청은 현재 대화가 총괄한다. 별도 Apply나 사용자에게 팀 사용을 다시 물을 필요 없이 아래 경로를 실행한다. 팀 파일의 provider/model/instructions를 실행 도구가 직접 읽으므로 플러그인 UI에서 총괄을 시작하지 않아도 동일 역할 정의를 사용한다.

1. 날짜·주제별 `docs/jobs/<job-id>/request.md`를 만든다. 원고·요구사항·실제 참고 경로·선택한 스타일을 담는다.
   기본 스킬은 fantasy-party-insta-toon이다. 다른 스타일을 선택했으면 모든 역할 실행에 `--skill <선택한-스킬-폴더명>`을 전달한다.
2. `python scripts/instatoon_team.py plan --job docs/jobs/<job-id>`를 실행한다. 반환 agentId로 로그와 완료 상태를 확인하고 plan.md가 실제 작성됐는지 읽는다.
3. 현재 세션이 선택한 이미지 스킬을 읽고 plan.md에 따라 image_gen으로 실제 이미지를 생성·저장한다. Paseo 원고 담당의 제안이 사용자 지시와 다르면 바로잡는다.
4. request.md에 검수 대상·참고·앵커 경로와 각각의 역할을 명시한 뒤 아래 QA 명령을 실행한다. 이미지 인수를 반복해 원본 참고와 앵커도 실제 첨부한다. 결과 보고서의 PASS를 확인하기 전 다음 장을 확정하지 않는다.
5. 수정은 현재 세션의 이미지 편집 도구로 수행하고 새 버전 파일과 새 보고서명을 사용한다. 장당 기본 2회 수정 후 남은 오류는 미완료로 보고한다.
6. 모든 장의 크기 보정과 최종 QA 후 caption 명령에 완성본을 모두 첨부한다. 실제 캡션 파일을 읽고 100~500자를 검사한 뒤 최종 경로로 복사한다. 이미지와 게시 원고를 함께 전달한다.

```powershell
python scripts/instatoon_team.py check
python scripts/instatoon_team.py plan --job docs/jobs/<job-id>
python scripts/instatoon_team.py qa --job docs/jobs/<job-id> --report qa-01-v1.md --image assets/YYYY-MM-DD/raw/01-topic.png --image refer/reference.png
python scripts/instatoon_team.py caption --job docs/jobs/<job-id> --image assets/YYYY-MM-DD/01-topic.png
.\scripts\paseo.ps1 wait <agent-id> --timeout 45
.\scripts\paseo.ps1 logs <agent-id> --tail 10
```

완료 대기는 45초 이하 단위로 진행하면서 사용자에게 진행 상황을 알린다. 작업 실패·중단·권한 거부 시 로그를 확인하고 원인을 해결하며 생성이나 QA를 완료로 꾸미지 않는다. 런처는 역할만 시작하므로 호출 세션이 반드시 결과 파일과 판정을 읽어 다음 단계를 진행해야 한다.

역할이 파일 도구 오류로 저장하지 못했지만 최종 응답에 완전한 원고/QA/캡션을 반환했다면 총괄이 해당 응답을 지정 파일에 저장하고 다시 읽어 확인한다. QA가 실제 이미지를 열지 못한 경우에는 이 방법으로 PASS를 만들어서는 안 된다. 런처는 원고와 실행 지침을 프롬프트에 직접 전달하고 Node로 실행하여 Windows 배치 파일의 여러 줄 인수 손실을 피한다.

Paseo 런타임의 읽기 전용 도구 점검에서 image_gen__imagegen과 view_image가 보고되었다. 실제 이미지 생성 호출의 성공까지 검증한 것은 아니다. 기본 경로는 현재 세션의 확실히 사용 가능한 이미지 도구를 사용한다. 이미지 도구가 있는 Paseo 제작 역할을 쓰려면 아래 완전 팀 경로로도 진행할 수 있다.

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

## Paseo UI에서 총괄을 시작하는 완전 팀 경로

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
