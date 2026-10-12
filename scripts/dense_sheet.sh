#!/bin/bash
# dense_sheet.sh <clip id e.g. 22_02_172> <seconds between frames> -> work/tmp/dense_<id>.jpg
p=$(ls work/proxies/*_$1_*.mp4); mkdir -p work/tmp
ffmpeg -v error -y -noautorotate -i "$p" -vf "fps=1/$2,scale=160:284,drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='%{pts\:hms}':x=3:y=3:fontsize=15:fontcolor=yellow:box=1:boxcolor=black@0.7,tile=8x${3:-3}" -frames:v 1 "work/tmp/dense_$1.jpg" 2>&1 | grep -v Fontconfig
