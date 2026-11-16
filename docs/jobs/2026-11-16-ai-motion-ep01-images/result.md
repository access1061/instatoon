# 1회차 이미지 제작 결과

상태: 완료. built-in image_gen으로 5장 제작, 부분 편집, 최종 크기 보정, Paseo 독립 시각 QA, 이미지 기준 캡션, 전달 ZIP을 완료했다. 게시·외부 발행은 하지 않았다.

## 전달 파일

패키지: `assets/2026-11-16/ai-motion-ep01-final.zip` (최종 PNG 5장·게시 캡션·README만 포함)

| 순서 | 최종 이미지 | QA |
| --- | --- | --- |
| 1 | assets/2026-11-16/ai-motion-ep01/01-course-question-v3.png | qa-01-v3.md — PASS |
| 2 | assets/2026-11-16/ai-motion-ep01/02-one-card.png | qa-02-v1.md — PASS |
| 3 | assets/2026-11-16/ai-motion-ep01/03-move-the-text-v3.png | qa-03-v3.md — PASS |
| 4 | assets/2026-11-16/ai-motion-ep01/04-learn-where-stuck.png | qa-04-v1.md — PASS |
| 5 | assets/2026-11-16/ai-motion-ep01/05-title-first.png | qa-05-v1.md — PASS |

게시 캡션: `assets/2026-11-16/ai-motion-ep01/instagram-caption-ai-motion-ep01.md` — 공백 포함 280자(저장 본문 기준). 별도 코드 블록·제목 없이 본문과 해시태그만 있다.

생성·편집 프롬프트: `assets/2026-11-16/ai-motion-ep01/prompts/`
생성 원본: 같은 폴더의 `raw/`. 이전 수정본은 보존하며 최종본 목록에는 넣지 않는다.

## 실제 제작·수정

사용자 참고 `refer/1116/chikawa.jpg`, `refer/1116/chikawa2.jpg`를 실제로 열고 이미지 도구에 입력했다. 둥근 얼굴·작은 몸·고유 귀와 색을 유지하고 크림 카디건·민트 후드·브라운 니트·연노랑 후드와 헤드폰을 적용했다.

1장: 스마트폰 앞뒤 혼재·신청 앞 망설이는 손동작·카디건 앞여밈을 두 번의 부분 편집으로 보완했다. v3 PASS 이후 해당 실제 파일을 후속 장의 스타일 앵커로 사용했다.
3장: 카드 겹침 관계와 하치와레의 첫 말풍선 꼬리를 두 번 부분 편집했다. 우사기는 '우라!'와 카드 이동 액션만 수행한다.
5장: 1장 앵커 외에 실제 3장 v3도 이미지 도구에 전달하여 우사기 의상·헤드폰을 이어갔다. 우사기는 '야하!'로만 반응한다.

## 검증 근거

- 모든 최종본은 지정 `fit_instagram_4x5.py`를 실행했다. raw는 1122×1402, final은 정확히 1080×1350.
- `verify_artifacts.py`로 같은 raw에서 비율 유지 축소와 흰 패딩 결과를 다시 계산해 최종본과 픽셀 일치를 확인했다. 자르기·늘이기를 하지 않았다. SHA256과 치수는 `artifact-verification.json`에 저장했다.
- 최종 이미지의 SHA256은 독립 QA가 실제로 본 임시 첨부 파일명과 일치한다. QA의 대상 버전과 저장소 최종본을 이 값으로 연결할 수 있다.
- 원고 역할과 QA 역할의 셸·Node 파일 읽기에는 환경 오류가 있었다. 필요한 지침·원고는 런처가 전문으로 전달했다. QA는 실제 첨부 이미지를 직접 열고 한글·화자·캐릭터·의미·가독성·앵커 연속성을 판정했다. 디스크 문서 직접 읽기나 독립 메타데이터 검사를 수행했다고 주장하지 않는다. 실제 픽셀·보정 검증은 총괄의 별도 검사다.
- 이미지 단위 최종 QA는 모두 PASS. 초기 REVISE 보고서와 수정 전 이미지도 남겼다.

## 캡션 실행의 복구

원본 작업에 누적된 QA 전문을 모두 포함하자 Windows 명령 길이 제한 WinError 206이 발생했다. 원본 보고서를 보존한 채 `docs/jobs/2026-11-16-ai-motion-ep01-caption/`에 최종 QA 출처 요약과 승인 계획 요약을 만들고, 실제 최종 이미지 5장을 다시 첨부해 Paseo caption 역할을 완료했다. 캡션 역할을 총괄 작성으로 몰래 대체하지 않았다.

## 역할 기록

- plan: ee31b27a-1ac2-4515-9b45-f84edb407e0a
- 1장 QA: 188eb976-622c-4323-82ff-8be6b3acc40b → 6464b53c-2ab8-48ea-bd3e-094907d381a5 → 8ae8f5ad-cdb1-4a61-98f2-5b7f2d1d9c5c
- 2장 QA: a14f46d4-9d89-49c3-9ec7-ab4329025012
- 3장 QA: 90610493-d458-4d5f-aa8c-b03f2c60a8df → fa4eefa2-5b85-4ef3-a68c-463156f37d76 → 03ada4d4-8e18-4098-afb0-4e20a4bc4c97
- 4장 QA: c2592ef4-5174-441e-ba89-a09ee36d938a
- 5장 QA: 8eec6ff9-846d-493d-a275-cd081b34b282
- caption: 7620d98b-ffd4-4521-afe4-d53de34a556d

다음 단계: 2회차 '예제에서 문구 하나 바꾸기'. `docs/series/ai-cardnews-motion/README.md`에 이어하기를 갱신했다. 1장 v3을 다음 회차 스타일 앵커로 재사용하며 같은 등장인물은 의상을 이어가거나 시간·장소 전환에 맞춰 명시적으로 바꾼다.
