---
title: 'neukit: automatic brain extraction and preoperative tumor segmentation from MRI'
colorFrom: indigo
colorTo: indigo
sdk: docker
app_port: 7860
emoji: 🧠
pinned: false
license: mit
app_file: app.py
---

<div align="center">
<h1 align="center">neukit</h1>
<h3 align="center">Automatic brain extraction and preoperative tumor segmentation from MRI</h3>

[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)
[![CI/CD](https://github.com/andreped/neukit/actions/workflows/deploy.yml/badge.svg)](https://github.com/andreped/neukit/actions/workflows/deploy.yml)
<a target="_blank" href="https://huggingface.co/spaces/andreped/neukit"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a>

**neukit** was developed by SINTEF Medical Image Analysis to accelerate medical AI research.

</div>

## Intro

This web application enables users to test [Raidionics](https://raidionics.github.io/), which is an open-source, free-to-use desktop application for pre- and postoperative central nervous system tumor segmentation and standardized reporting. The app only supports single volume input and only demonstrates the segmentation results of the Raidionics software, and thus is only meant for demonstration purposes.

For postoperative tumor segmentation, standardized reporting, and better functionality for performing analysis on full cohorts (batch mode), please, refer to the Raidionics software which is hosted [here](https://github.com/raidionics/Raidionics).

## Demo <a target="_blank" href="https://huggingface.co/spaces/andreped/neukit"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a>

To access the live demo, click on the `Hugging Face` badge above. Below is a snapshot of the current state of the demo app.

<img width="1722" alt="Screenshot 2023-06-06 at 21 53 25" src="https://github.com/andreped/neukit/assets/29090665/e67f35c2-482b-409c-b1a9-bc987fbb5c6a">

## Development

Alternatively, you can deploy the software locally. Note that this is only relevant for development purposes. Simply dockerize the app and run it:

```
docker build -t neukit .
docker run -it -p 7860:7860 neukit
```

Then open `http://127.0.0.1:7860` in your favourite internet browser to view the demo.

## Citation

If you found the tool useful in your research, please, cite the corresponding software paper:

```
@misc{bouget2023raidionics,
    title={Raidionics: an open software for pre- and postoperative central nervous system tumor segmentation and standardized reporting}, 
    author={David Bouget and Demah Alsinan and Valeria Gaitan and Ragnhild Holden Helland and André Pedersen and Ole Solheim and Ingerid Reinertsen},
    year={2023},
    eprint={2305.14351},
    archivePrefix={arXiv},
    primaryClass={physics.med-ph}
}
```
