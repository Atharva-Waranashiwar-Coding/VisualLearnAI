# VisualLearn AI

A free, local-first visual microlearning prototype. Open `index.html` in a browser or serve it from any static host.

## Features

- Four interactive sample lessons: Binary Search, Neural Networks, HTTP Requests, Spaced Repetition
- Three-step visual lesson player, quizzes, XP, streaks, review reminders
- Progress stored locally in browser localStorage
- Experimental on-device AI lesson generation using WebLLM and WebGPU, without a paid API key
- Responsive single-page app, no build step or backend required

## Run locally

```bash
python3 -m http.server 8000
```

Visit http://localhost:8000. Use a modern Chromium browser for the optional WebGPU AI mode. AI mode downloads a large model and can be slow or unsupported on some devices. Offline mode supports only the included topics. The model may generate inaccurate explanations.

## Deploy for free

Publish the repository as a static site using GitHub Pages or Cloudflare Pages. For Cloudflare Pages, use no build command and `/` as the output directory. GitHub Pages: Settings > Pages > Deploy from a branch > main > root.

## Current limitations

This is an MVP, not a production-ready adaptive learning system. It does not offer accounts, server-side sync, citations, arbitrary interactive diagram generation, or guaranteed browser AI availability. Progress is specific to one browser and can be lost if site data is cleared. No paid API is required, but model downloads and device computation are not free of resource use.

## License

MIT license recommended if publishing as open source; no license file has been added yet.
