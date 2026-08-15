SRT 자막이 손그림 영상으로 바뀌는 오픈소스 마법을 써봤어.

`srt-whiteboard-animation`은 자막 순서에 맞춰 그림 영역을 나누고, 공중의 펜이 선을 따라 그린 뒤 색을 더해 MP4로 렌더링하는 Codex 스킬이야. 미리보기 화면에서 영역·순서·시간을 조정할 수도 있음.

사용 흐름은 저장소 복제 → `prepare_env.py` → `parse_srt.py` → 선화와 `annotation.json` 준비 → `preview.html` 확인 → `render_stream_whiteboard.py` 실행. 기본 권장 장면 길이는 25~35초지만 이번에는 10초 단일 장면으로 만들었어.

GitHub: https://github.com/geeklee/srt-whiteboard-animation

#오픈소스 #SRT #화이트보드애니메이션 #AI영상 #CodexSkill #인스타툰
