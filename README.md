# VisualLearnAI: AI-narrated video microlearning

Vertical, swipeable microlearning for system design, AI engineering, software engineering and technical interview preparation.

## Implemented
- Full-screen 9:16 video feed with swipe, keyboard navigation, playback, mute, saves, quizzes and local progress.
- Published MP4 playback with animated browser previews until rendering is complete.
- 8 structured career lessons with scripted narration, visual node sequences, and quizzes.
- Python + Pillow motion-graphics renderer, espeak-ng synthesized voice, FFmpeg MP4 encoding.
- Automated daily video generation and publishing via GitHub Actions at 11:15 UTC, plus manual workflow dispatch.
- Static hosting compatible with GitHub Pages or Cloudflare Pages. No paid API keys.

## Run locally
```bash
python3 -m http.server 8000
```
Open http://localhost:8000. Before publishing, the browser displays animated previews with browser-generated speech.

## Generate videos
Install Python 3, Pillow, ffmpeg, espeak-ng and a DejaVu font. Then:
```bash
python3 -m pip install pillow
python3 scripts/render_videos.py --limit 4
```
This writes `videos/*.mp4` and `content/manifest.json`.

## Automate publishing
Open **Actions > Generate and publish daily learning videos > Run workflow** to create the initial MP4 files. Scheduled runs follow the workflow cron, subject to GitHub Actions scheduling and quota constraints. GitHub Pages must be enabled separately under **Settings > Pages**. Scheduled workflows can be delayed or disabled due to repository inactivity.

## What is and isn't AI
Narration uses a local speech synthesizer, not a neural TTS voice. The current content pipeline animates **authored structured lessons**; it does not autonomously write novel lessons with a language model. This provides a zero-API-fee baseline and a functional daily video-publishing workflow. True LLM-based script/storyboard generation, content fact-checking, better neural voices, personalization across devices, and large-scale media hosting remain future work. A daily rotation reuses the lesson bank rather than guaranteeing new topics forever.

## Prior versions
The previous card-based MVP remains in `legacy.html`.
