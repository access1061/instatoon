# Paseo Agent Team 인스타툰 제작 결과

원문: https://gyuha.com/post/2026/11/2026-11-03-paseo-agent-team/
보조 자료: https://paseo.sh/plugins/gyuha/agent-team

## 최종 이미지 (게시 순서)

1. assets/2026-11-04/01-paseo-agent-team.png — 시안과 구현의 차이
2. assets/2026-11-04/02-paseo-agent-team.png — 별도 검수 역할 추가
3. assets/2026-11-04/03-paseo-agent-team-v2.png — 영역 비교와 수정 전달
4. assets/2026-11-04/04-paseo-agent-team.png — 개선 결과와 한계

네 파일 모두 Pillow로 실제 1080×1350을 확인했다. 원본은 raw/에 보존하고 기존 fit_instagram_4x5.py로 비율 유지 축소·흰 여백 보정했다. 최종본은 생성 원본을 자르거나 늘이지 않았다.

## 생성·검수

- 스킬: fantasy-party-insta-toon, imagegen. 기본 내장 image_gen 사용.
- 원고 기획: Paseo editor ea69ac4b-30b5-48ca-a477-48e03b3c26b2. 가독성을 위해 총괄이 대사를 축약하고 plan.md에 반영.
- 실제 첫 입력 참고: assets/2026-08-13/instagram-4x5/01-free-stock-mcp-hook-instagram.png. 이 이미지의 캐릭터·선·채색만 반영.
- 첫 장 PASS 후 01-paseo-agent-team.png를 후속 장의 실제 생성 입력 앵커로 사용. 3·4장에는 2장도 보조 입력.
- 생성 프롬프트: assets/2026-11-04/prompts/01~04-paseo-agent-team.txt 및 03-paseo-agent-team-v2-edit.txt.
- 1장: qa-01-v1.md PASS.
- 2장: qa-02-v1.md PASS.
- 3장: qa-03-v1.md REVISE. 전달 카드가 정상→오류 방향으로 읽혀 오류→개선으로 부분 편집했고 태블릿의 비율·배경 스케치와 배경 검수 연결선을 수정. qa-03-v2.md PASS. 기존 03-paseo-agent-team.png는 탈락본으로 보존하며 게시용 묶음에 제외.
- 4장: qa-04-v1.md PASS.
- 모든 QA는 Paseo visual-qa 역할이 실제 원본·보정본·참고·앵커 이미지를 열어 비교했다. 역할의 셸 문서 읽기는 도우미 오류로 실패해 런처가 직접 전달한 문서 전문을 사용했고 보고서에 제한을 기록했다. 이미지 열람은 정상 동작했다. 별도 픽셀 크기 검사는 총괄이 수행했다.

## 캡션·전달

게시 캡션: assets/2026-11-04/instagram-caption-paseo-agent-team.md
원본 캡션 초안: 이 작업 폴더의 caption.md
최종 캡션은 Paseo 초안을 바탕으로 총괄이 스킬의 반존대 정보체에 맞게 편집하고, 공식 요구 버전과 원문 출처를 보충했다.
Paseo 캡션 담당: bfb35c9c-1bb8-44d0-87de-75da697b45bf
전달 묶음: assets/2026-11-04/paseo-agent-team-instagram.zip (최종 4장과 캡션만)

본 결과는 원문 사례를 새 장면·대사로 각색했다. 원문의 게임 스크린샷을 복제하지 않았다. 실제 게시·Git 공개는 수행하지 않았다.
