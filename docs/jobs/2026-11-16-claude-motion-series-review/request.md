# 원고 검토 및 시리즈 방향 설정

사용자 요청: E:\Pi_workspace\naver_blog 자료를 참고해 인스타툰 시리즈를 제작하되, 먼저 원고 검토와 방향을 설정한다. 이번 단계는 기획까지이며 이미지 생성·발행은 진행하지 않는다.

## 읽을 자료
- E:/Pi_workspace/naver_blog/final/blog/01_start.md
- E:/Pi_workspace/naver_blog/final/blog/02_install.md
- E:/Pi_workspace/naver_blog/final/blog/03_plan.md
- E:/Pi_workspace/naver_blog/final/blog/04_code.md
- E:/Pi_workspace/naver_blog/final/blog/05_motion.md
- E:/Pi_workspace/naver_blog/final/blog/06_review.md
- E:/Pi_workspace/naver_blog/final/review/VALIDATION.md
- E:/Pi_workspace/naver_blog/final/review/REVIEW.md
- E:/Pi_workspace/naver_blog/source/SERIES_GUIDE.md (초기안 대조용)

## 요청하는 산출물
plan.md에 한국어로 원고 검토, 6회 연재 방향, 회차별 핵심 메시지와 짧은 장별 대사 초안을 작성한다. 이미지와 캡션은 아직 만들지 않는다. 원본 파일은 수정하지 않는다.

## 편집 방향
- 대상: AI로 콘텐츠를 만들고 싶지만 코드·영상 도구가 낯선 초보 제작자.
- 주제: Claude Code와 웹 기술로 카드뉴스를 만들고 모션그래픽으로 확장하는 제작 과정.
- 기본안: 판타지 3인 파티, 컬러 4:5, 6회 연재 × 회당 4장(총 24장, 제안값).
- 은발 안내자는 절차, 붉은 머리 행동가는 오해·실패, 보라 머리 분석가는 범위와 검증을 담당.
- 치이카와는 원자료 속 예제 소재다. 사용자에게 치이카와를 진행 캐릭터로 선택받았다고 간주하지 않는다.
- 1회 결과와 도구 역할, 2회 준비와 점검, 3회 사실과 카드 기획, 4회 그림·글자 레이어와 수정, 5회 정보 전달용 움직임, 6회 오류와 검수·재사용.
- 각 회차에 독자 질문 하나, 실수 하나, 실행 기준 하나를 둔다. 코드와 설치 명령 전체는 블로그에 남긴다.

## 검토에서 반드시 반영할 사실과 한계
- final을 기준으로 하며 source의 16초·3.2초 구성과 섞지 않는다. 완성 예제는 정지 5장과 24초 영상이며 인스타툰 연재 회차/장수와 다르다.
- 각 편 앞에 추가된 모션 설명이 입문 흐름을 끊는다. 인스타툰에서는 기본 제작→모션 확장 순으로 재구성한다.
- HyperFrames render는 해당 환경에서 완료되지 않았고 실제 MP4는 HTML/GSAP→Edge 프레임 캡처→FFmpeg 경로다. 렌더 성공·속도 일반화 금지.
- 검수 문서에 청감 검수 미수행이 명시됨. 음악까지 검증 완료라고 쓰지 않는다.
- VALIDATION.md와 REVIEW.md의 모션 추가 부분에는 실제 물음표로 깨진 문장이 있어 해당 부분을 근거 문구로 재사용하지 않는다.
- Claude가 실제 제작을 전부 수행했다는 대화 로그가 없다. 재현용 프롬프트와 로컬 실행 결과를 구분한다.
- 행사 일정은 제공 자료의 예시이며 공식 최신 공지를 검증한 것이 아니다. 이번 기획에서는 일정과 예약 정보를 최신 방문 안내로 재발행하지 않는다.
- 최신 설치법·버전의 정확성은 이번 로컬 원고 편집 검토만으로 인증하지 않는다. 구체 명령을 인스타툰에 싣기 전 공식 자료 재확인 필요.
- 스크린샷·실제 이미지에 대한 독립 Visual QA는 이번 단계의 범위가 아니다.
