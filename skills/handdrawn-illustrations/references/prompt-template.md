# 이미지 생성 프롬프트 템플릿

각 그림은 따로 생성한다. 본문 내용에 맞춰 변수를 채우고, 여러 장을 한 이미지에 합치지 않는다.

> 이미지 모델은 영어 구조 프롬프트 + 한글 라벨 조합에서 가장 안정적이다. 아래 프롬프트 본문은 영어로 두되, 화면에 들어갈 손글씨 주석만 한글로 지정한다.
> 캐릭터 묘사(`character description`)는 `references/character-ip.md`의 정의를 그대로 옮긴다. 캐릭터를 바꿨다면 이 줄도 함께 바뀐다.

```text
Generate one standalone 16:9 horizontal Korean article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art with slightly thick marker-like lines. Slightly wobbly pen lines, uneven line weight, casual hand-drawn Instagram toon feeling. Lots of empty white space. Sparse red/orange/blue handwritten Korean annotations only when useful. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no children's illustration, no realistic UI.

Recurring IP character required:
{character description — 캐릭터 IP의 외형/성격을 영어로. 기본 캐릭터 예시: a small modern everyday human character, big head and small body, simple memorable hair silhouette, dot eyes or short line eyes, tiny mouth, basic hoodie or sweatshirt, cute but calm Instagram toon style, drawn with slightly thick black hand-drawn lines}. The character must perform the core conceptual action, not decorate the scene. Make the character friendly and cute, but keep the article meaning more important than cuteness.

Theme:
{본문 삽화 주제}

Structure type:
{구조 유형: Workflow / 시스템 국부 / 전후 대비 / 역할 상태 / 개념 은유 / 방법 계층 / 지도 경로 / 짧은 만화 컷}

Core idea:
{이 그림이 표현할 핵심 의미}

Composition:
{구체적 화면: 캐릭터가 어디서 무엇을 하는지, 주요 사물은 무엇인지, 정보가 어떻게 흐르는지}

Suggested elements:
{요소1} / {요소2} / {요소3} / {요소4}

Korean handwritten labels (write these exactly, keep them short):
{주석어1} / {주석어2} / {주석어3} / {주석어4} / {선택 주석어5}

Color use:
Black for main line art and the character. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Korean labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, dense explainer, fantasy character art, or polished webtoon key visual. Use a modern everyday person character, not fantasy ears, horns, wings, magic props, armor, or decorative accessories. It should feel like a short hand-drawn Instagram toon panel that explains the article meaning through the character's action.
```

## 이미지 편집 프롬프트

좌측 상단 제목 제거:

```text
Edit the provided image. Remove only the handwritten title "{지울 글자}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

기이함 강화:

```text
Regenerate this illustration with the same core meaning and simple layout, but make the character more central to the conceptual action. The character should be doing the work that explains the idea, not standing beside the diagram. Keep it clean, sparse, hand-drawn, modern, and Instagram-toon-like.
```

## 한글 라벨 안정화 팁

- 이미지 모델은 한글 글자에서 오타·환각이 자주 난다. 라벨은 **짧을수록** 안정적이다 (2~6자 권장).
- 오타가 나면 라벨 개수를 줄이고 재생성하는 것이 정석.
- 핵심 단어 1~2개는 라벨로, 나머지는 형태/구도로 표현해 글자 의존도를 낮춘다.
