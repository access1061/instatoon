<!-- forge-slug: generate-ai-agent-solopreneur-instatoon-carousel -->
<!-- task: 2 -->
<!-- priority: high -->
<!-- tdd: off -->
# AI 에이전트 1인 창업 원칙 인스타툰 5장 제작

## 목표 / 제외 범위
- 목표: 확정된 콘티를 바탕으로 고정 3인 판타지 파티가 등장하는 컬러 4:5 인스타툰 5장과 100~500자 게시 원고를 제작한다.
- 목표: 각 장을 최종 1080×1350 PNG로 맞추고, 캐릭터·스타일·핵심 의미·짧은 한글 문구를 검수해 `assets/2026-09-13/`에 저장한다.
- 제외 범위: 콘티의 논지 재기획, 새로운 창업 사례 조사, 블로그 원문 수정, 실제 인스타그램 계정 게시·업로드는 하지 않는다.

## 기준 자료
- 콘티: `assets/2026-09-13/ai-agent-solopreneur-instatoon-storyboard.md`
- 시각 기준: `assets/2026-08-13/instagram-4x5/01-free-stock-mcp-hook-instagram.png` 외 같은 폴더의 3장
- 캐릭터·화면 문법: `fantasy-party-insta-toon`의 `references/visual-dna.md`
- 생성·검수 기준: `fantasy-party-insta-toon`의 프롬프트 템플릿과 QA 체크리스트
- 관련 ADR: 없음
- 완료 정의: 아래 5개 최종 PNG가 모두 1080×1350이고 열 수 있으며, 동일한 3인 파티와 밝은 컬러 4:5 문법을 유지하고, 각 장의 제목·대사·핵심 의미가 콘티와 일치한다. `assets/2026-09-13/instagram-caption-ai-agent-solopreneur.md`에는 그림 대사를 반복하지 않는 100~500자 본문, 2026-09-12 자료 기준·성과 비보장 고지, 해시태그 3~8개가 있다.
  - `assets/2026-09-13/01-ai-coding-is-not-business-instagram.png`
  - `assets/2026-09-13/02-distribution-first-instagram.png`
  - `assets/2026-09-13/03-two-week-mvp-instagram.png`
  - `assets/2026-09-13/04-ai-agent-automation-instagram.png`
  - `assets/2026-09-13/05-solopreneur-checklist-instagram.png`

## 작업 단위
- [ ] S1. 시각 기준 이미지와 콘티 1장을 참조해 첫 장을 생성하고 스타일 앵커를 확정한다. — 완료 기준: 1장 원본과 1080×1350 최종본이 있으며 캐릭터 3인의 외형, 순백 배경, 제한 팔레트, 큰 상황 컷, 제목과 짧은 대사가 확인된다.
- [ ] S2. 첫 장을 연속성 앵커로 다시 참조해 2~5장을 한 장씩 생성한다. — 완료 기준: 각 장이 별도 이미지이고, 콘티의 `유통 우선 → 2주 MVP → AI 자동화 → 체크리스트` 의미와 동일 캐릭터가 유지된다. (의존: S1)
- [ ] S3. 한글·과밀도·캐릭터 일관성을 검사하고 가까운 결과는 부분 편집한 뒤, 모든 최종본을 비율 유지 방식으로 1080×1350에 맞춘다. — 완료 기준: 5개 파일의 실제 크기가 모두 1080×1350이다. (의존: S2)
