# 이미지 생성 프롬프트

사용자의 표현을 먼저 유지하고, 참고 이미지가 있으면 실제 이미지 입력으로 전달한다. 관찰하지 않은 스타일 특성을 추측해 추가하지 않는다.

```text
Generate one standalone {aspect ratio} Korean illustration.

User intent:
{사용자가 원하는 결과를 한두 문장으로 요약}

Reference use:
{참고 이미지에서 반영할 선·색·비율·표정·구도·캐릭터 특징 3~6개}
{스타일만 참고할지, 캐릭터도 유지할지 명시}

Character:
{외형, 고정 색상, 표정, 포즈와 장면 행동}

Scene:
{한 장의 핵심 의미와 간결한 배치}

Text to render exactly:
- Speech: "{짧은 문구 또는 없음}"
- Overlay: "{짧은 문구 또는 없음}"
- Labels: "{필요한 주석 또는 없음}"

Keep consistent:
{시리즈에서 유지할 캐릭터와 스타일 특징}

Avoid only these unintended changes:
{사용자가 원하지 않거나 참고 이미지와 충돌하는 요소만 짧게 명시}
Do not add unrequested text.
```

인스타 피드·캐러셀이면 `{aspect ratio}`에 `exact 4:5 portrait, 1080x1350`을 넣는다. 생성 후 실제 크기는 반드시 `scripts/fit_instagram_4x5.py`로 정규화한다.

## 에피소드형 요청에만 추가

```text
Fixed protagonist:
{이름/역할, 머리 실루엣, 얼굴, 의상과 색, 대표 소품, 성격 결함, 반복 행동}

Episode beat:
{문제 / 욕망·오해 / 반전·판단 / 해결·콜백 중 이 장의 역할}

Emotional beat:
{당황, 기대, 경계, 안도, 허탈과 이를 보여주는 표정·행동}

Continuity:
Repeat the fixed character traits exactly. Use the prior approved image only for character and style continuity; create a new composition. Convey facts through action, reaction, and short speech rather than a static row of labels. Keep the character original and do not imitate a named artist, franchise, or copyrighted character.
```

사용자가 특정 감정 연출이나 만화 문법을 원하면 `references/episode-toon.md`의 일반적 특성으로 번역해 넣는다. 사용자 참고 이미지가 있으면 그 특성과 충돌하는 기본 감정 기호나 흑백 선화를 강제하지 않는다.

## 생성 팁

- 스타일 재현이 어려우면 텍스트와 소품이 없는 간단한 스타일 앵커를 먼저 만든다.
- 승인된 앵커와 원본 참고 이미지를 이후 장에 함께 전달한다.
- 결과가 가까우면 전체 재생성보다 “머리 비율 확대”, “선 굵기 변경”처럼 한 번에 한 특성만 편집한다.
- 한글이 틀리면 문구를 줄여 한 번 재생성하고, 계속 틀리면 해당 영역을 부분 편집한다.
