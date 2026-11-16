"""Record delivered PNG sizes and verify the prescribed fit operation."""
from pathlib import Path
import hashlib
import json
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[3]
ASSETS = ROOT / 'assets/2026-11-16/ai-motion-ep01'
NAMES = ['01-course-question-v3', '02-one-card', '03-move-the-text-v3',
         '04-learn-where-stuck', '05-title-first']

records = []
for name in NAMES:
    raw = ASSETS / 'raw' / (name + '.png')
    final = ASSETS / (name + '.png')
    with Image.open(raw) as source, Image.open(final) as result:
        expected = source.convert('RGB')
        original_size = expected.size
        expected.thumbnail((1080, 1350), Image.Resampling.LANCZOS)
        canvas = Image.new('RGB', (1080, 1350), 'white')
        canvas.paste(expected, ((1080 - expected.width) // 2,
                                (1350 - expected.height) // 2))
        assert result.size == (1080, 1350), (name, result.size)
        assert ImageChops.difference(canvas, result.convert('RGB')).getbbox() is None, name
        records.append({'file': str(final.relative_to(ROOT)),
                        'raw_size': original_size, 'final_size': result.size,
                        'fit_verified': True,
                        'sha256': hashlib.sha256(final.read_bytes()).hexdigest()})

report = Path(__file__).with_name('artifact-verification.json')
report.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(records, ensure_ascii=False, indent=2))
