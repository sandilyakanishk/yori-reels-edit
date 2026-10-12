#!/bin/bash
# Build 720x1280 SDR proxies from the 4K HLG phone clips (run from project root).
mkdir -p work/proxies
for f in Flow_VID_*.mov; do
  out="work/proxies/${f%.mov}.mp4"
  [ -s "$out" ] && continue
  rot=$(ffprobe -v error -select_streams v:0 -show_entries stream_side_data=rotation -of default=nw=1:nk=1 "$f" | head -1)
  if [ "$rot" = "90" ]; then tr="transpose=cclock"; else tr="transpose=clock"; fi
  ffmpeg -v error -y -noautorotate -hwaccel cuda -i "$f" \
    -vf "scale=1280:720:flags=bilinear,$tr,zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p" \
    -c:v h264_nvenc -preset p4 -cq 26 -g 15 -c:a aac -b:a 96k -metadata:s:v rotate=0 "$out.tmp.mp4" && mv "$out.tmp.mp4" "$out" && echo "done $f"
done
echo ALLDONE
