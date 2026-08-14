# 이미지 생성 프롬프트

각 장을 별도 이미지로 생성한다. 기준 캐러셀과 첫 안정 결과를 실제 참고 이미지로 전달한 뒤 아래 변수를 채운다.

```text
Generate one standalone exact 4:5 portrait Korean Instagram carousel image.

Series continuity:
Use the provided reference images for the same three-character fantasy party, clean line quality, soft cel coloring, proportions, and speech-bubble layout. Preserve the fixed hair, eyes, ears, clothes, palette, and role of each recurring character. Create a new composition for this page.

Fixed party:
- Silver-haired elven guide: {이번 장의 표정과 행동}
- Red-haired energetic actor: {이번 장의 표정과 행동}
- Purple-haired calm analyst: {이번 장의 표정과 행동}

Page role:
{호기심 / 설명 / 설정 / 활용 / 제한·반전 / 결론}

Core fact:
{원고에서 확인한 사실 하나}

Scene:
{1~2개의 큰 컷, 캐릭터 행동, 노트북·카드·표 등 소품 배치}

Text to render exactly:
- Speech 1: "{짧은 문구}"
- Speech 2: "{짧은 문구}"
- Speech 3: "{필요한 경우}"
- Overlay: "{정확한 정보 또는 없음}"
- Labels: "{짧은 라벨 또는 없음}"

Constraints:
Pure white background, thin clean black outlines, soft flat cel colors, 2-to-3-head-tall mini characters, rounded speech bubbles, generous safe margins, and no cropping of heads, ears, hands, or text. Keep one information role and one emotional role on this page. Do not add unrequested text, logos, names, titles, watermarks, or extra characters.
```

한글이 틀리면 문구를 줄여 한 번 재생성한다. 전체가 가깝다면 잘못된 말풍선이나 특징만 부분 편집한다.
