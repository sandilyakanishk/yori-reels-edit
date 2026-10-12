# Analysis of the two posted reels (@meetyori)

Source files (not in the repo): `Video-80949.mp4` = Episode 1, `Video-33553.mp4` = Episode 2.
Contact sheets (1 frame per second, timestamped) are in `context/reference/`.

## Series so far

| | Episode 1 (`80949`) | Episode 2 (`33553`) |
|---|---|---|
| Length | 81.4 s | 46.5 s |
| Format | 720x1280, 30 fps | 720x1280, 30 fps |
| Shots | 19 (avg 4.3 s) | 18 (avg 2.5 s) |
| Story | Old iPhone 6s lying around -> turn it into a desk AI companion -> roadmap -> UI inspiration -> prompts -> Antigravity generates the website | Website -> app. App UI design system, Flutter build, first version runs on the phone, teases the "brain" layers |
| Ends on | Desk wide shot with the Yori site on the monitor, no end card | Black end card: Yori face icon + "Meet Yori" + "@meetyori" (~3 s) |

Episode 2 is the tighter one (half the length, faster cuts, end card). The new reel should follow Episode 2.

## Visual style

- Vertical phone footage, handheld, shot at the desk at night. Warm tungsten room light + blue/pink LED glow. Nothing is graded heavily.
- **No on-screen text or captions at all.** The only graphic is the end card in Episode 2.
- **Hard cuts only.** No transitions, no zooms added in post, no speed ramps.
- Shot vocabulary, repeated in both reels:
  1. Desk / setup establishing shot (posters, pegboard, monitor + laptop)
  2. Monitor close-ups filmed off-screen at an angle (website, design system, code)
  3. Direct screen recordings, full-frame (app screens, ChatGPT prompt) used as 1 s flashes
  4. Top-down notebook shot, hand writing the plan with a marker ("App UI 1st draft", "UI -> Brain")
  5. Hands: typing on the purple/red keyboard, mouse, holding the phone
  6. One lifestyle / personality shot (on the beanbag with the dog; back-of-head at desk)
  7. An "artsy" b-roll shot near the end (screen reflected in sunglasses, rack focus)
- Yori itself (black phone, two white eyes, red dot mouth) appears early and again at the end.
- Episode 2 rhythm: 3.0 s shots for the first 22 s (cuts at 3.3, 6.3, 9.3, 12.2, 15.3, 18.3, 21.2), then 3.5-4 s shots, then a burst of ~1 s shots (35.5-38.6) before the end card at 43.1.

## Narration (voice-over)

Language: Hinglish. Hindi sentence frame, English nouns/tech words. Episode 2 switches to full English for the last third.

Measured:

| | Episode 1 | Episode 2 |
|---|---|---|
| Words | 258 in 80.5 s | 119 in 42.9 s |
| Pace | 3.2 words/s | 2.8 words/s |
| Pauses >= 0.35 s | 4 (0.8-1.3 s, at section changes) | 1 (0.44 s) |
| Pitch | median 139 Hz (127-154) | median 136 Hz (126-148) |
| Loudness | -14.3 LUFS, range 5.7 LU | -14.7 LUFS, range 2.3 LU |

- Voice is calm, conversational, low and flat (pitch only moves ~25 Hz). No hype voice. It reads like talking to a friend ("yaar", "honestly").
- Voice-over is wall-to-wall: it starts on frame 1 and runs until the end card. No silent b-roll sections.
- A quiet, bassy music bed runs under the whole thing, roughly 15-18 dB below the voice. Almost no high-frequency content (audio is 66 kbps AAC, energy above 3.4 kHz is about 1%).
- Sentences are 2-3.5 s long, and in Episode 2 each sentence maps to roughly one shot.

### Script structure (same in both)

1. **Context hook** - where things stand ("yaar mere paas kaafi time se ek iPhone 6s...", "last video mein maine Yori introduce kara tha...")
2. **Goal for this episode** ("ab mujhe iski website ko ek app mein convert karna tha")
3. **Steps, in order**: "sabse pehle...", "iske baad...", "phir...", "uske baad..."
4. **Result + honest reaction** ("first look mein mujhe kaafi accha laga", "yeah it's looking good")
5. **What's still left / the challenge** ("abhi isme kaafi kaam baaki hai", "but the main challenge is...")
6. **Forward-looking close** ("ab dekhte hain...", "that's the part I'm really excited about")

### Transcripts

**Episode 1**

> Yaar mere paas kaafi time se ek iPhone 6s bas aise hi pada tha, aur honestly iska koi use bhi nahi tha. Aur aajkal main kaafi AI companions dekh raha tha, jo log apne setup pe rakhte hain, dekhne mein kaafi clean lagta hai aur isse workspace ka kaafi aesthetic bhi badh jaata hai. To maine socha jab mere paas ek phone already pada hai to kyun na main isko bhi ek AI companion bana doon. Sabse pehle maine iska ek rough roadmap banaya. Iske baad maine kuch websites dekhna start kari. Main chahta tha iska UI thoda simple, minimal, aur dekhne mein aisa lage ki ye setup ka ek part hai. Main kisi aur AI ya chatbot ka look nahi lena chahta tha, to maine bas alag-alag jagah se ideas lena start kare aur unko combine kara. Phir maine AI ki help lena start kari, iska ek website aur basic design dene ke liye kuch maine prompts likhwaye. Aur phir maine prompt copy karke Antigravity ko diya, phir usne mera ek website generate kara, aur honestly first look mein mujhe kaafi accha laga. Abhi ye bhi final bilkul nahi hai, lekin direction ekdum waise hi ja raha hai jaise maine socha tha. Abhi isme kaafi kaam baaki hai: chatbot banana hai, automation lagane hain, baaki jo backend tools kaam karenge wo lagane hain, apne AI ke face ke liye emotions bhi banane hain. Aur aaj se maine iski shuruaat kari hai. Ab dekhte hain isko main kitna aage le ja sakta hoon.

(The last sentence is partly unclear in the recording.)

**Episode 2**

> Last video mein maine Yori introduce kara tha aur uski ek basic si website banayi thi. Ab mujhe iski website ko ek app mein convert karna tha jisme main apna chatbot laga sakoon. To is baar maine iska ek app UI prepare karna start kara. Pehle maine basic layout screen decide kari: colors, buttons, overall experience. Uske baad maine Flutter use kara, and finally the first version of the app starts running. And yeah, it's looking good. But the main challenge is ab mujhe iske backend mein multiple layers lagani hain automation ke liye. And once these layers start working together, then I'll see how Yori will actually work, and that's the part I'm really excited about.

## What the story promised for Episode 3

- Episode 1 to-do list: chatbot, automation, backend tools, **emotions for the face**.
- Episode 2 cliffhanger: the backend "layers" (notebook page: UI -> Brain: speech -> speech-to-text -> brain layer -> API request -> response -> emotion engine -> Yori speaks with an emotion) starting to work together.
