# VisualLearn AI: personalized career learning feed

A local-first, Instagram-style microlearning website focused on **system design, AI engineering, software engineering, and technical interviews**.

## What's implemented
- Responsive career-learning feed with four tracks and **28 authored, structured micro-lessons**.
- Daily rotation of four curriculum posts, based on the learner's local calendar and start date.
- Visual three-node diagrams, knowledge-check quizzes, saved posts, XP, daily progress and streaks.
- Personalization of tracks, learning level, name, and daily goal.
- Optional **on-device AI lesson generation** using WebLLM and WebGPU, with structured output validation. Generated lessons join today's feed and are stored locally.
- Local browser persistence and JSON backup export.
- Original proof-of-concept preserved at [legacy.html](legacy.html).

## Run
Open `index.html` in a browser or serve it locally:
```bash
python3 -m http.server 8000
```
Open http://localhost:8000.

## Free hosting
GitHub Pages: repository **Settings > Pages > Deploy from a branch > main > root**. No build command is required. Cloudflare Pages can also publish the root directory.

## How daily content works
The app ships with a curated lesson bank for reliable daily delivery without any external API or paid inference. The daily selection changes by calendar date. The user can optionally generate additional AI-authored posts locally on a compatible device; those posts are not automatically generated while the browser is closed.

## Honest limitations
This is a complete **single-browser MVP**, not a production multi-user service. No accounts, server database, hosted inference, background daily AI generation, or cross-device synchronization. The AI button requires WebGPU and a large model download, may fail on unsupported devices, and AI output must be fact-checked. Browser localStorage can be cleared. The curated lesson bank rotates after its concepts are exhausted; it is not an infinite stream of novel content.

## Roadmap
1. Server-side scheduled AI lesson generation with a free/self-hosted model and content validation.
2. Auth and Postgres persistence for cross-device sync.
3. Adaptive scheduling using mastery and spaced repetition.
4. Interactive visual component registry beyond simple flow diagrams.
5. Content evaluation and moderation before publishing.

No paid API keys are required for the current MVP.
