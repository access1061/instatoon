# 완료: 2화 원하는 배치를 구체적으로 요청하기

## 최종 캡션 제목 수정
사용자 피드백으로 캡션 첫 줄에 ‘AI 카드뉴스 2화 | 원하는 배치를 구체적으로 요청하기’를 추가했다. 최신 캡션은 공백 포함 306자, 최신 패키지는 ai-motion-ep02-layout-final-v2.zip이다. 이전 제목 없는 캡션이 포함된 ZIP은 기록으로 보존한다. manifest.json과 새 ZIP의 캡션 글자 수 검사 통과.

사용자가 최종 지정한 E:/Pi_workspace/naver_blog/final/blog/03_plan.html을 실제 읽고 4장으로 각색. 02_install.html 기반 시안은 취소하고 보존. 이미지 생성과 마지막 장 부분 편집은 현재 세션 built-in image_gen 사용. Paseo 원고·장별 독립 시각 QA·캡션 역할 실행 완료.

최종 파일 폴더: assets/2026-11-16/ai-motion-ep02/layout/
1. 01-be-specific.png — qa-01-v2.md PASS
2. 02-specify-layout.png — qa-02-v1.md PASS
3. 03-fix-the-symptom.png — qa-03-v1.md PASS
4. 04-review-and-record-v2.png — qa-04-v2.md PASS

게시 캡션: instagram-caption-ai-motion-ep02.md, 공백 포함 273자. caption 역할은 2026-11-17-ai-motion-ep02-layout-caption job으로 실행하고 총괄이 종결 어투만 반존대로 편집했다. 원고/검수 전문을 모두 한 명령에 넣자 Windows 길이 제한이 발생하여 요약 인계의 별도 캡션 job으로 해결.

패키지: assets/2026-11-16/ai-motion-ep02/ai-motion-ep02-layout-final.zip. 최종 4장·캡션·README·manifest·프롬프트 포함. 취소 시안과 수정 전 4장은 제외.

package.py 검증 통과: 4장 실제 1080×1350, 원본 비율 유지 LANCZOS 축소+흰 여백 예상 결과와 픽셀 일치, 잘라내기·늘이기 없음, 네 보고서 PASS, 캡션100~500자. 원본은 layout/raw/와 generated_images에 보존. manifest.json에 실제 원본 크기와 QA 매핑 기록.

QA는 실제 대상·앵커·참고를 열어 검수했다. QA 역할의 문서 읽기와 메타데이터 측정 일부가 환경 오류로 실패한 제한은 각 보고서에 공개했다. 정확한 치수와 보정 픽셀 비교는 총괄이 별도 실행했다. 실제 CSS 수정/실행 인증이 아닌 팬 각색 교육용 이미지이며 외부 발행은 하지 않았다.
