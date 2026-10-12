import sys, json
from faster_whisper import WhisperModel
m = WhisperModel("large-v3", device="cpu", compute_type="int8", cpu_threads=8)
prompt = "Yaar, last video mein maine Yori introduce kiya tha. AI companion, website, app, UI, Flutter, prompt, Antigravity, ChatGPT, iPhone 6s, setup."
for f in sys.argv[1:]:
    segs, info = m.transcribe(f, beam_size=5, language="hi", word_timestamps=True, vad_filter=False, initial_prompt=prompt, condition_on_previous_text=False)
    out=[]
    print("==", f, flush=True)
    for s in segs:
        print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text.strip()}", flush=True)
        out.append({"s":s.start,"e":s.end,"t":s.text,"w":[[w.start,w.end,w.word] for w in (s.words or [])]})
    json.dump(out, open(f+".json","w",encoding="utf-8"), ensure_ascii=False)
