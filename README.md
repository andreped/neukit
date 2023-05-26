---
title: 'neukit: automatic meningioma segmentation from T1-weighted MRI'
colorFrom: indigo
colorTo: indigo
sdk: docker
app_port: 7860
emoji: 🔎
pinned: false
license: mit
app_file: app.py
---

# neukit

## Usage

The software will be made openly available on Hugging Face spaces very soon. Stay tuned for more!

## Setup

For development of this software, follow these steps to build the docker image and run the app through it:

```
docker build -t neukit ..
docker run -it -p 7860:7860 neukit
```

Then open `http://127.0.0.1:7860` in your favourite internet browser to view the demo.
