"""Verify final dimensions, captions and QA before making a delivery archive."""
from pathlib import Path
import json
import zipfile
import shutil
from PIL import Image, ImageChops

root = Path(__file__).resolve().parents[3]
job = Path(__file__).resolve().parent
out = root / 'assets/2026-11-16/ai-motion-ep02/layout'
names = ['01-be-specific.png', '02-specify-layout.png', '03-fix-the-symptom.png', '04-review-and-record-v2.png']
reports = ['qa-01-v2.md', 'qa-02-v1.md', 'qa-03-v1.md', 'qa-04-v2.md']
generated = Path('C:/Users/Administrator/.codex/generated_images/01a1e850-ce24-7b53-be99-cb88a4644d2a')
sources = ['exec-8eb04557-6e5b-4e2f-8412-e7ef456c836e.png', 'exec-ef66a72a-4858-48fe-aee9-32a36e28c180.png', 'exec-30463814-8f93-4284-9501-6f6c9629cc2f.png', 'exec-f8deb73d-4488-4d64-beb8-7ffe1d24966a.png']
(out / 'raw').mkdir(exist_ok=True)
records = []
for name, report, source in zip(names, reports, sources):
    raw_path = out / 'raw' / name
    if not raw_path.exists():
        shutil.copy2(generated / source, raw_path)
    with Image.open(raw_path) as original:
        source_size = list(original.size)
        scaled = original.convert('RGB')
        scaled.thumbnail((1080, 1350), Image.Resampling.LANCZOS)
        expected = Image.new('RGB', (1080, 1350), 'white')
        expected.paste(scaled, ((1080-scaled.width)//2, (1350-scaled.height)//2))
    with Image.open(out / name) as im:
        assert im.size == (1080, 1350), (name, im.size)
        assert ImageChops.difference(im.convert('RGB'), expected).getbbox() is None, name
        records.append({'image': name, 'size': list(im.size), 'source_size': source_size, 'fit_without_crop_or_stretch': True, 'qa': report})
    assert '판정: PASS' in (job / report).read_text(encoding='utf-8-sig'), report
caption_path = out / 'instagram-caption-ai-motion-ep02.md'
if not caption_path.exists():
    shutil.copy2(job.parent / '2026-11-17-ai-motion-ep02-layout-caption/caption.md', caption_path)
caption = caption_path.read_text(encoding='utf-8-sig').strip()
assert 100 <= len(caption) <= 500, len(caption)
manifest = {'source': 'E:/Pi_workspace/naver_blog/final/blog/03_plan.html', 'images': records, 'caption_characters': len(caption), 'published': False}
(out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
archive = out.parent / 'ai-motion-ep02-layout-final.zip'
version = 2
while archive.exists():
    archive = out.parent / f'ai-motion-ep02-layout-final-v{version}.zip'
    version += 1
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for name in names + [caption_path.name, 'README.md', 'manifest.json', 'prompts.md']:
        z.write(out / name, name)
print(json.dumps({'archive': str(archive), **manifest}, ensure_ascii=False, indent=2))
