# Yori reels - edit workspace

Edit context and scripts for the @meetyori Instagram reels (building Yori, an AI desk companion on an old iPhone).

Raw footage, proxies and rendered videos are **not** in this repo (too large). Copy the `Flow_VID_*.mov` clips into the project root on the other PC, then run the scripts.

## Layout

- `context/01-reel-analysis.md` - breakdown of the two posted reels: shots, pacing, narration style, transcripts
- `context/02-clip-log.md` - every raw clip: what it is, usable or not
- `context/03-ep3-edit.md` - the Episode 3 cut: shot list + voice-over draft
- `edit/` - edit lists (EDL json) and the end card
- `context/reference/` - 1-frame-per-second contact sheets of the posted reels
- `context/clips/` - contact sheets of the raw clips for the new reel
- `scripts/` - ffmpeg / Python helpers (proxies, contact sheets, transcription, audio stats, render)

## Requirements

ffmpeg (with zscale + tonemap, NVENC optional), Python 3.11 with Pillow and numpy. `scripts/transcribe.py` needs `pip install faster-whisper`.

Run everything from the project root in Git Bash:

```bash
bash scripts/make_proxies.sh
```

```bash
python scripts/contact_sheets.py
```
