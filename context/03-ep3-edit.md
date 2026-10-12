# Episode 3 cut - "giving Yori a brain"

Edit list: `edit/ep3_edl.json`. Render: `python scripts/render.py edit/ep3_edl.json` (add `--proxy` for a fast draft).
Output: `output/yori_ep3_final.mp4`, 1080x1920, 30 fps, 50.3 s, **silent** (voice-over and music go on top).

Style rules taken from the posted reels: hard cuts only, no text on screen, ~3 s shots, one burst of 1 s shots before the close, 3.2 s "Meet Yori" end card. See `01-reel-analysis.md`.

## Shot list

| Time | Shot | Clip |
|---|---|---|
| 0.0-3.0 | Hook: macro of Yori's face, blink at 2.0 | 025144 |
| 3.0-6.0 | Notebook: Basic Architecture (voice -> input -> brain -> prompt -> response -> text to speech -> display with emotions) | 024406 |
| 6.0-9.0 | Desk wide, code on both screens | 014821 |
| 9.0-12.0 | NVIDIA build: "Start Building Your AI Here" | 031856 |
| 12.0-15.0 | Llama model list | 031946 |
| 15.0-17.6 | Clicking "Generate API Key" | 032314 |
| 17.6-20.8 | Architecture diagram on the monitor | 033233 |
| 20.8-22.2 | Prompt scroll: "15. YORI BRAIN" | 034530 |
| 22.2-23.3 | Prompt: "Thinking -> Yori Thinking face" | 034530 |
| 23.3-24.5 | Prompt: "NVIDIA request construction" | 034530 |
| 24.5-27.9 | Agent thinking + Dart code | 014349 |
| 27.9-30.9 | Laptop keyboard glow | 015738 |
| 30.9-34.1 | You with headphones, holding Yori | 023411 |
| 34.1-37.5 | Testing the app in hand | 045811 |
| 37.5-40.5 | Yori standing in front of the monitor (punched in) | 022556 |
| 40.5-43.5 | Burst: face macro / desk figurine / face macro | 025256, 050234, 025256 |
| 43.5-47.1 | Yori on the notebook, "Talk to Yori", blink | 025359 |
| 47.1-50.3 | End card: Meet Yori @meetyori | edit/endcard.png |

## Voice-over draft (to rewrite in your own words)

Target: about 130-140 words, 2.8-3.2 words per second, start on frame 1, finish by 47.1 s. Same structure as before: where we are -> goal -> steps -> result -> what's left -> close. The lines in square brackets are guesses from the footage; fix them.

| Time | Line |
|---|---|
| 0.0-3.0 | Last video mein Yori ka app chal gaya tha, lekin abhi tak ye bas ek face tha. |
| 3.0-6.0 | To is baar maine iska brain banana start kara. Sabse pehle ek basic architecture likha. |
| 6.0-9.0 | Voice se input, input se brain, aur brain se response. |
| 9.0-15.0 | Brain ke liye mujhe ek AI model chahiye tha, to maine NVIDIA ke free models dekhe [aur Llama 3.3 choose kara]. |
| 15.0-17.6 | Phir iski API key generate kari. |
| 17.6-20.8 | Uske baad maine pura flow design kara, kaunsi layer kya karegi. |
| 20.8-24.5 | Aur ek detailed prompt likha: brain, prompt builder, aur har emotion ke liye ek face. |
| 24.5-30.9 | Phir AI ne code likhna start kara. [Honestly isme kaafi bugs aaye, aur kaafi time laga.] |
| 30.9-37.5 | And finally, maine isko phone pe test kara. |
| 37.5-43.5 | [And yeah, it's working. Yori ab reply kar sakta hai.] |
| 43.5-47.1 | [Next step: isko apni awaaz dena.] Let's see how far this goes. |

Audio notes for matching the old reels: voice at about -14.5 LUFS integrated, quiet bassy music bed about 15-18 dB under the voice, no gaps longer than ~1 s.
