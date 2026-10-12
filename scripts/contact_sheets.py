"""Contact sheets of the proxies: one row of 8 frames per clip, 3 clips per sheet.
Usage: python scripts/contact_sheets.py   (run from project root, after make_proxies.sh)"""
import glob, os, subprocess, json
from PIL import Image, ImageDraw, ImageFont
N, W, H = 8, 160, 284
os.makedirs("work/tmp", exist_ok=True); os.makedirs("context/clips", exist_ok=True)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 15)
rows = []
for p in sorted(glob.glob("work/proxies/Flow_VID_*.mp4")):
    if p.endswith(".tmp.mp4"): continue
    cid = os.path.basename(p)[18:24]          # HHMMSS, e.g. 014349
    dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]))
    row = Image.new("RGB", (N*W, H+22), "black"); d = ImageDraw.Draw(row)
    d.text((4, 2), f"{cid}   {dur:.1f}s", fill="yellow", font=font)
    for i in range(N):
        t = dur*(i+0.5)/N; f = f"work/tmp/{cid}_{i}.jpg"
        subprocess.run(["ffmpeg","-v","error","-y","-noautorotate","-ss",f"{t:.2f}","-i",p,"-frames:v","1","-vf",f"scale={W}:{H}",f])
        row.paste(Image.open(f), (i*W, 22)); d.text((i*W+4, 24), f"{t:.1f}", fill="yellow", font=font, stroke_width=2, stroke_fill="black")
    rows.append(row)
for k in range(0, len(rows), 3):
    grp = rows[k:k+3]; sheet = Image.new("RGB", (N*W, (H+22)*len(grp)))
    for j, r in enumerate(grp): sheet.paste(r, (0, j*(H+22)))
    sheet.save(f"context/clips/sheet_{k//3+1:02d}.jpg", quality=80)
print(len(rows), "clips")
