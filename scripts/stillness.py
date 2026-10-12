"""Print per-0.2s motion for a clip proxy (low = camera/screen is still). Usage: python scripts/stillness.py 034530"""
import sys, glob, subprocess, numpy as np
p = glob.glob(f"work/proxies/*_{sys.argv[1]}_*.mp4")[0]
raw = subprocess.run(["ffmpeg","-v","error","-noautorotate","-i",p,"-vf","fps=5,scale=90:160,format=gray","-f","rawvideo","-"],capture_output=True).stdout
f = np.frombuffer(raw, np.uint8).reshape(-1, 160, 90).astype(np.float32)
d = np.abs(np.diff(f, axis=0)).mean(axis=(1, 2)); b = f.mean(axis=(1, 2))
for i in range(0, len(d), 5):
    print(f"{i/5:5.1f}s  motion " + " ".join(f"{x:4.1f}" for x in d[i:i+5]) + f"   bright {b[i]:.0f}")
