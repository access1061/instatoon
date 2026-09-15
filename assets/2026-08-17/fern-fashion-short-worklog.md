# Fern Fashion Short 작업 기록

## 최종 결과

- 영상: `fern-fashion-short-9x16.mp4`
- 해상도: 1080×1920
- 화면 비율: 9:16
- 길이: 8.000초
- 프레임레이트: 30fps
- 영상 코덱: H.264 High Profile, yuv420p
- 음성 코덱: AAC, 32kHz, 모노
- 콘셉트: 일본 패션 매거진 스틸컷이 천천히 살아나는 세로형 AI 샘플

## 사용 소스

- 최초 4:5 캐릭터 이미지: `01-fern-hiphop-personal-color-v2.png`
- 9:16 확장 이미지: `fern-fashion-magazine-9x16-source.png`
- TTS WAV: `fern_fashion_0817_clean.wav`
- TTS 길이: 정확히 8.000초, 32kHz 모노
- 세로형 자막: `fern-fashion-short.ass`
- TTS 연기 지침: `tts-direction-fern-fashion-short.md`
- 재렌더링 스크립트: `render-fern-fashion-short.ps1`

## 9:16 이미지 생성 방향

- Fern을 화면 왼쪽에 배치하고 오른쪽을 세로 자막 안전 영역으로 확보한다.
- 얼굴, 긴 보라색 머리, 블랙 오버사이즈 스트리트웨어, 실버 체인과 빈손을 유지한다.
- 지팡이와 무기는 넣지 않는다.
- 배경은 흰 종이, 차콜·딥 퍼플 사선, 재단선, 점과 십자 기호, 약한 하프톤으로 구성한다.
- 이미지 생성 단계에서는 글자·숫자·로고를 넣지 않고 편집 단계에서만 타이포를 합성한다.

## 영상 타임라인

| 구간 | 연출 | 텍스트 |
|---|---|---|
| 0.15–1.30초 | 페이드인, 매거진 레이블 | `ISSUE 08` |
| 0.50–3.70초 | 느린 줌, 첫 음성 자막 | `似合う色は / 静かに私を / 強くする` |
| 3.72–4.35초 | 보라색 라이트 스캔 | `DEEP WINTER` |
| 4.30–7.62초 | 두 번째 음성 자막 | `今日は / 少しだけ / 大胆に` |
| 7.45–8.00초 | 페이드아웃, 엔드 레이블 | `QUIET MAGIC / FERN` |
| 0.20–7.80초 | AI 샘플 고지 | `AI CONCEPT SAMPLE` |

## 시각 효과

- 전체 8초 동안 약 2.5%의 느린 중심 줌
- 아주 미세한 아래 방향 카메라 이동
- 3.72–4.32초 사이 반투명 보라색 라이트 스캔
- 약한 시간 기반 필름 그레인
- 시작 0.25초 페이드인, 종료 0.35초 페이드아웃
- 일본어 세로 자막은 Yu Gothic Bold 사용
- 기본 자막은 딥 플럼, 강조어 `強くする`, `大胆に`는 로열 퍼플 계열 사용

## 재렌더링

PowerShell에서 다음 명령을 실행한다.

```powershell
powershell -ExecutionPolicy Bypass -File .\assets\2026-08-17\render-fern-fashion-short.ps1
```

소스 이름을 바꿀 때는 매개변수를 지정한다.

```powershell
powershell -ExecutionPolicy Bypass -File .\assets\2026-08-17\render-fern-fashion-short.ps1 `
  -Background "new-background.png" `
  -Audio "new-voice.wav" `
  -Subtitle "new-titles.ass" `
  -Output "new-short.mp4"
```

## QA 결과

- 영상 스트림: 1080×1920, 30fps, H.264
- 오디오 스트림: AAC, 32kHz, 모노
- 최종 길이: 정확히 8.000초
- 일본어 글꼴 렌더링 정상
- 자막이 얼굴을 가리지 않음
- 캐릭터의 머리와 손이 프레임 안에 유지됨
- 지팡이·무기 없음
- AI 샘플 표기 포함

## 재사용 시 주의점

- 새 음성의 길이가 8초가 아니면 ASS 타임코드와 `-t 8` 값을 함께 수정한다.
- 인물 위치가 달라지면 자막의 `\\pos(x,y)` 좌표를 조정한다.
- 세로쓰기에서 문장부호가 어색하면 기호를 별도 이벤트로 분리한다.
- Instagram 업로드 시 플랫폼의 AI 콘텐츠 공개 설정을 확인한다.

## V2 잡지 커버 수정

- 배경: `fern-fashion-magazine-cover-v2-source.png`
- 자막: `fern-fashion-short-cover-v2.ass`
- 영상: `fern-fashion-short-cover-v2-9x16.mp4`
- 방향: 클래식 월간 애니메이션 잡지 커버의 정보 구조를 참고하되 실제 제호 로고는 복제하지 않았다.
- 고정 제호: `NEW TYPE`, `2026 AUGUST / VOL.01`, `FERN`, `今月の主役`
- `FERN`과 `今月の主役`을 상단 우측의 핵심 표지 정보로 배치했다.
- 음성 자막 크기를 기존 58–64px에서 74–84px로 확대했다.
- 강조어 `強くする`, `大胆に`는 밝은 라벤더로 분리했다.
- 원본 V1 파일은 비교와 재사용을 위해 그대로 보존했다.

## V3 에디토리얼 쇼츠

- 배경: `fern-fashion-magazine-9x16-source.png`
- 자막: `fern-fashion-short-v3.ass`
- 영상: `fern-fashion-short-v3-9x16.mp4`
- 재렌더링 스크립트: `render-fern-fashion-short-v3.ps1`
- QA 스냅샷: `qa-v3-01.png`, `qa-v3-02.png`, `qa-v3-03.png`
- 특징: 머리 위 대형 `FERN` 제호, 상단 룩북 헤더, 우측 세로 대사.

## V4 Refer1 포스터 스타일 쇼츠 (그래픽 포스터 룩)

- 참고 스타일: `refer1.jpg` (드래곤볼 18호 캐릭터 매거진 포스터 레이아웃)
- 배경: `fern-fashion-magazine-9x16-source.png`
- 자막: `fern-fashion-short-v4-poster.ass`
- 영상: `fern-fashion-short-v4-poster-9x16.mp4`
- 재렌더링 스크립트: `render-fern-fashion-short-v4-poster.ps1`
- QA 스냅샷: `qa-v4-01.png`, `qa-v4-02.png`, `qa-v4-03.png`

### 접목 특징
1. **상단 대형 제호 (Top Masthead)**: `DRAGON BALL`처럼 화면 상단 너비를 꽉 채우는 볼드 와이드 타이포 `FRIEREN`과 영문 에디토리얼 인용구 배치.
2. **좌측 세로 대형 텍스트**: `人造人間 18号` 문법을 차용하여 좌측 여백에 `一級魔法使い 08`을 굵은 세로 한자 및 볼드 넘버로 배치해 그래픽 포스터로서의 강렬한 아이덴티티 확립.
3. **우측 세로 대사 동기화**: 페른의 8초 음성 호흡에 맞춰 1부/2부 대사와 로열 라벤더 하이라이트(`強くする`, `大胆に`)가 순차적으로 등장.
4. **우측 하단 스펙 카드 & 바코드**: `refer1.jpg`의 캐릭터 스펙 박스를 오마주한 `FERN NO.08 / SPECIAL EDITION LOOKBOOK / DEEP & COOL WINTER` 및 바코드 그래픽 배치.
5. **하단 메인 서명 로고**: `Fern` 필기체/세리프 로고와 `DEEP WINTER STREET EDITION ★★★` 언더라인으로 하단 안정감 완성.


