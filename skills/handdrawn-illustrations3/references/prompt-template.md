# 이미지 생성 프롬프트 템플릿

각 그림은 따로 생성한다. 본문 내용에 맞춰 변수를 채우고, 여러 장을 한 이미지에 합치지 않는다.

한 장으로 의미가 과밀해지면 2~4장으로 나눠 생성한다. 나누는 기준은 핵심 앵커다: 문제 제기, 라우팅/선택, 진단/대체, 결과/주의처럼 서로 다른 판단이 있으면 별도 이미지로 분리한다. 각 이미지는 하나의 핵심 의미만 담는다.

> gpt image-gen은 한글 말풍선과 텍스트 오버레이를 비교적 안정적으로 생성한다. 화면에 들어갈 핵심 한글 문구는 후처리로 분리하지 말고 생성 프롬프트에 함께 넣는다.

```text
Generate one standalone 16:9 horizontal Korean article illustration.

Visual DNA:
Pure white background. Black thin felt-tip pen line art only. No coloring. No shading. No gradients. No 3D effects. Slightly wobbly hand-drawn lines with uneven line weight, like a quick clean sketch in a notebook. Lots of empty white space. Simple 1 to 3 small comic-like situation panels. Do not make it look like a polished vector illustration, PPT infographic, formal flowchart, children's poster, or webtoon key visual.

Line style references:
Use assets/sample-line-style.png and assets/sample-line-style-2.png only as style references for thin but clear black pen line quality, loose sketch touch, chibi big-head small-body proportions, small simplified hands and feet, simple repeated hair strokes, wide 3-panel spacing, sparse handwritten Korean labels, small arrows, check marks, and sorting boxes. Do not copy their fantasy characters, elf ears, pointed ears, capes, jewelry, fantasy costumes, or fantasy props.

Character required:
A modern adult mini human character, big head and small body in the same chibi proportion style as the two references, simple face with dot eyes or short line eyes and a tiny mouth, calm understated expression, small simplified hands and feet. Gender can be male or female depending naturally on the article context. Use modern everyday or work clothes such as shirt, hoodie, knit, jacket, slacks, jeans, sneakers. The character must perform the core action: checking, comparing, organizing, warning, choosing, recording, or solving. The character must not stand in a corner as decoration.

Strict character bans:
No elf ears, no pointed ears, no fairy, no wizard, no fantasy race, no horns, no wings, no tail, no cape, no armor, no magic wand, no magic effects, no fantasy jewelry. Use normal rounded human ears only.

Theme:
{본문 삽화 주제}

Structure:
{1~3개의 작은 상황 컷 / 전후 대비 / 짧은 과정 / 선택과 정리 / 경고와 해결 중 하나}

Core idea:
{이 그림이 표현할 핵심 의미}

Composition:
{캐릭터가 어디서 무엇을 확인·비교·정리·경고·선택·기록·해결하는지. 주요 소품은 스마트폰, 노트북, 서류, 체크리스트, 카드, 박스, 앱 화면 등 현대 소품 중 1~3개만 사용}

Korean text to render exactly:
- Speech bubble 1: "{짧은 말풍선 문장}"
- Speech bubble 2: "{짧은 말풍선 문장 또는 생략}"
- Text overlay: "{핵심 요약 1~2줄 또는 생략}"
- Small labels: "{짧은 주석어1}" / "{짧은 주석어2}" / "{선택 주석어3}"

Constraints:
One image explains one core meaning. Preserve at least 35% blank white space. Render the Korean text exactly as provided in the speech bubbles, text overlay, and small labels. Keep each speech bubble to one short sentence and each overlay to one or two short lines. Do not add extra text. Do not write a top-left title unless it is explicitly included in Korean text to render exactly. Do not write the structure type on the image. Keep the scene modern, simple, monochrome, and readable from the character's action.
```

## 한글 텍스트 안정화 팁

- gpt image-gen에서는 말풍선, 텍스트 오버레이, 짧은 주석어를 생성 단계에서 함께 넣는다.
- 정확해야 하는 문구는 `Korean text to render exactly` 아래에 따옴표로 명시한다.
- 말풍선은 한 문장 이하, 텍스트 오버레이는 1~2줄 중심으로 쓴다.
- 한 장에 문구가 많아지면 후처리하지 말고 이미지를 2~4장으로 분리한다.
- 생성 결과의 한글이 실제로 깨지거나 오배열되면 먼저 문구를 줄여 재생성하고, 그래도 해결되지 않을 때만 후처리 조판을 사용한다.
