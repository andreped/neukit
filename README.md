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

## Demo <a target="_blank" href="https://huggingface.co/spaces/andreped/neukit"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a>

![Screenshot 2023-06-05 at 17 31 48](https://github.com/andreped/neukit/assets/29090665/f184fda5-b9db-48fb-b096-dd589e8fce81)

## Setup

For development of this software, follow these steps to build the docker image and run the app through it:

```
docker build -t neukit .
docker run -it -p 7860:7860 neukit
```

Then open `http://127.0.0.1:7860` in your favourite internet browser to view the demo.
