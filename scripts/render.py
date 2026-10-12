"""Render an EDL to a vertical reel.
  python scripts/render.py edit/ep3_edl.json --proxy   -> quick 720x1280 draft from work/proxies
  python scripts/render.py edit/ep3_edl.json           -> final 1080x1920 from the 4K HLG originals
Run from the project root. Output goes to output/. Video only + silent audio track (voice-over is added later)."""
import json, sys, os, glob, subprocess
edl = json.load(open(sys.argv[1])); proxy = "--proxy" in sys.argv
W, H = (720, 1280) if proxy else (1080, 1920)
fps = edl["fps"]; tmp = "work/tmp/render_" + ("proxy" if proxy else "final"); os.makedirs(tmp, exist_ok=True); os.makedirs("output", exist_ok=True)
TONEMAP = "zscale=t=linear:npl=200,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv"
parts = []
for i, s in enumerate(edl["segments"]):
    out = f"{tmp}/{i:02d}.mp4"; parts.append(out)
    grade = f",eq=gamma={s['gamma']}" if "gamma" in s else ""
    crop = ""                      # optional punch-in: "crop": [centre_x, centre_y, zoom] in 0..1 of the upright frame
    if "crop" in s:
        cx, cy, z = s["crop"]; crop = f"crop=iw/{z}:ih/{z}:(iw-iw/{z})*{(cx-0.5/z)/(1-1/z):.4f}:(ih-ih/{z})*{(cy-0.5/z)/(1-1/z):.4f},"
    if proxy:
        src = glob.glob(f"work/proxies/*_{s['clip']}_*.mp4")[0]
        vf = f"{crop}scale={W}:{H}{grade},fps={fps},format=yuv420p"
    else:
        src = glob.glob(f"Flow_VID_*_{s['clip']}_*.mov")[0]
        rot = subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream_side_data=rotation","-of","default=nw=1:nk=1",src]).decode().split()[0]
        tr = "transpose=cclock" if rot == "90" else "transpose=clock"
        vf = f"{tr},{crop}scale={W}:{H}:flags=lanczos,{TONEMAP}{grade},fps={fps},format=yuv420p"
    cmd = ["ffmpeg","-v","error","-y","-noautorotate","-display_rotation","0","-ss",str(s["in"]),"-i",src,"-t",str(s["dur"]),"-an","-vf",vf,
           "-frames:v",str(round(s["dur"]*fps)),"-c:v","libx264","-preset","medium","-crf","14" if not proxy else "20","-map_metadata","-1",out]
    subprocess.run(cmd, check=True); print("seg", i, s["clip"], s["note"], flush=True)
if "endcard" in edl and os.path.exists("edit/endcard.png"):
    out = f"{tmp}/zz_end.mp4"; parts.append(out); d = edl["endcard"]["dur"]
    subprocess.run(["ffmpeg","-v","error","-y","-loop","1","-i","edit/endcard.png","-t",str(d),"-vf",f"scale={W}:{H}:flags=lanczos,fps={fps},format=yuv420p",
                    "-c:v","libx264","-preset","medium","-crf","14" if not proxy else "20",out], check=True)
lst = f"{tmp}/list.txt"; open(lst,"w").write("".join(f"file '{os.path.abspath(p).replace(os.sep,'/')}'\n" for p in parts))
final = f"output/{edl['name']}_{'draft' if proxy else 'final'}.mp4"
subprocess.run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",lst,"-f","lavfi","-i","anullsrc=r=48000:cl=stereo",
                "-c:v","libx264","-preset","slow" if not proxy else "veryfast","-crf","20" if not proxy else "22","-pix_fmt","yuv420p",
                "-colorspace","bt709","-color_primaries","bt709","-color_trc","bt709","-c:a","aac","-b:a","128k","-shortest","-movflags","+faststart",final], check=True)
print("wrote", final)
