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

## 생성 팁

- 스타일 재현이 어려우면 텍스트와 소품이 없는 간단한 스타일 앵커를 먼저 만든다.
- 승인된 앵커와 원본 참고 이미지를 이후 장에 함께 전달한다.
- 결과가 가까우면 전체 재생성보다 “머리 비율 확대”, “선 굵기 변경”처럼 한 번에 한 특성만 편집한다.
- 한글이 틀리면 문구를 줄여 한 번 재생성하고, 계속 틀리면 해당 영역을 부분 편집한다.
