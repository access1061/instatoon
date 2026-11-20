from pathlib import Path
from PIL import Image
import json
import shutil
import zipfile

root = Path(__file__).resolve().parents[3]
job = Path(__file__).resolve().parent
out = root / 'assets/2026-11-20/ebook-chaos-party'
names = ['01-ebook-intro-v3', '02-first-card', '03-ask-again-v2', '04-motion-export', '05-free-ebook']
reports = ['qa-01-v4.md', 'qa-02-v1.md', 'qa-03-v2.md', 'qa-04-v1.md', 'qa-05-v1.md']
records = []
for name, report in zip(names, reports):
    target = out / f'{name}.png'
    raw = out / 'raw' / f'{name}.png'
    assert '판정: PASS' in (job / report).read_text(encoding='utf-8-sig')
    with Image.open(raw) as src, Image.open(target) as final:
        assert final.size == (1080, 1350), (name, final.size)
        fitted = src.convert('RGB')
        fitted.thumbnail((1080, 1350), Image.Resampling.LANCZOS)
        expected = Image.new('RGB', (1080, 1350), 'white')
        expected.paste(fitted, ((1080-fitted.width)//2, (1350-fitted.height)//2))
        assert expected.tobytes() == final.convert('RGB').tobytes(), name
        records.append({'image': target.name, 'size': list(final.size), 'raw_size': list(src.size), 'qa': report, 'verdict': 'PASS', 'uncropped_fit_verified': True})
caption = (job / 'caption.md').read_text(encoding='utf-8-sig').strip()
assert 100 <= len(caption) <= 500, len(caption)
caption_path = root / 'assets/2026-11-20/instagram-caption-ebook-chaos-party.md'
assert not caption_path.exists(), caption_path
caption_path.write_text(caption + '\n', encoding='utf-8')
shutil.copy2(caption_path, out / caption_path.name)
shutil.copy2(job / 'plan.md', out / 'scenario.md')
manifest = {'images': records, 'caption_characters': len(caption), 'caption': caption_path.name, 'reference_anchor': names[0]+'.png', 'notes': '독립 시각 QA PASS. 크기 및 비율 유지 전체 보존은 총괄이 Pillow로 별도 검증. 공개 발행은 하지 않음.'}
(out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
archive = root / 'assets/2026-11-20/ebook-chaos-party.zip'
with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as z:
    for name in names:
        z.write(out / (name+'.png'), name+'.png')
    for name in ['scenario.md', caption_path.name, 'manifest.json']:
        z.write(out / name, name)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == 8
(job / 'result.md').write_text('# 완료 결과\n\n5장 이미지와 게시 캡션 완료. 모든 최종본 독립 시각 QA PASS 및1080×1350·원본 비율 유지 전체 보존 검증 완료.\n\n'+ '\n'.join(f'- {r["image"]}: {r["qa"]} PASS' for r in records) + f'\n\n캡션 {len(caption)}자.\n묶음: {archive}\n시나리오: {out / "scenario.md"}\n캡션: {caption_path}\n\n이전 버전은 보존. QA 역할의 셸 초기화 오류로 독립 메타데이터 검사는 불가했으나 실제 이미지 열람은 성공. 총괄이 최종 크기와 raw 대비 보정 픽셀을 검증함. 미해결 필수 수정 없음. 발행하지 않음.\n', encoding='utf-8')
print(json.dumps({'images': records, 'caption_characters': len(caption), 'zip': str(archive), 'zip_bytes': archive.stat().st_size}, ensure_ascii=False))
