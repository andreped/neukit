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
<a target="_blank" href="https://huggingface.co/spaces/andreped/neukit"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a><a href="https://colab.research.google.com/gist/andreped/f83e53b120ddc2f6930f1dd66a16f248/neukit-demo-example.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

**neukit** was developed by SINTEF Medical Image Analysis to accelerate medical AI research.

</div>

## Brief intro

This web application enables users to test [Raidionics](https://raidionics.github.io/), which is an open-source, free-to-use desktop application for pre- and postoperative central nervous system tumor segmentation and standardized reporting. The app only supports single volume input and only demonstrates the segmentation results of the Raidionics software, and thus is only meant for demonstration purposes.

For postoperative tumor segmentation, standardized reporting, and better functionality for performing analysis on full cohorts (batch mode), please, refer to the Raidionics software which is hosted [here](https://github.com/raidionics/Raidionics).

## Demo <a target="_blank" href="https://huggingface.co/spaces/andreped/neukit"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a>

To access the live demo, click on the `Hugging Face` badge above. Below is a snapshot of the current state of the demo app.

<img width="1722" alt="Screenshot 2023-06-06 at 21 53 25" src="https://github.com/andreped/neukit/assets/29090665/e67f35c2-482b-409c-b1a9-bc987fbb5c6a">

## Development

### Docker

Alternatively, you can deploy the software locally. Note that this is only relevant for development purposes. Simply dockerize the app and run it:

```
docker build -t neukit .
docker run -it -p 7860:7860 neukit
```

Then open `http://127.0.0.1:7860` in your favourite internet browser to view the demo.

### Python

It is also possible to run the app locally without Docker. Just setup a virtual environment and run the app.
Note that the current working directory would need to be adjusted based on where `neukit` is located on disk.

```
git clone https://github.com/andreped/neukit.git
cd neukit/

virtualenv -ppython3 venv --clear
source venv/bin/activate
pip install -r requirements.txt

python app.py --cwd ./
```

### CoLab

To aid people developing in the cloud, we have made a simple Jupyter Notebook example which is hosted on Google CoLab.

Click the badge above to access it. This is mainly of interest to developers.

## Troubleshooting

Due to `share=True` being enabled by default when launching the app,
internet access is required for the app to be launched. This can disabled by setting
the argument to `--share 0`.

## Citation

If you found neukit relevant in your research, please cite the following references.

The final software including updated performance metrics for preoperative tumors and introducing postoperative tumor segmentation:
```
@article{bouget2023raidionics,
    author = {Bouget, David and Alsinan, Demah and Gaitan, Valeria and Holden Helland, Ragnhild and Pedersen, André and Solheim, Ole and Reinertsen, Ingerid},
    year = {2023},
    month = {09},
    pages = {},
    title = {Raidionics: an open software for pre-and postoperative central nervous system tumor segmentation and standardized reporting},
    volume = {13},
    journal = {Scientific Reports},
    doi = {10.1038/s41598-023-42048-7},
}
```

For the preliminary preoperative tumor segmentation validation and software features:
```
@article{bouget2022preoptumorseg,
    title={Preoperative Brain Tumor Imaging: Models and Software for Segmentation and Standardized Reporting},
    author={Bouget, David and Pedersen, André and Jakola, Asgeir S. and Kavouridis, Vasileios and Emblem, Kyrre E. and Eijgelaar, Roelant S. and Kommers, Ivar and Ardon, Hilko and Barkhof, Frederik and Bello, Lorenzo and Berger, Mitchel S. and Conti Nibali, Marco and Furtner, Julia and Hervey-Jumper, Shawn and Idema, Albert J. S. and Kiesel, Barbara and Kloet, Alfred and Mandonnet, Emmanuel and Müller, Domenique M. J. and Robe, Pierre A. and Rossi, Marco and Sciortino, Tommaso and Van den Brink, Wimar A. and Wagemakers, Michiel and Widhalm, Georg and Witte, Marnix G. and Zwinderman, Aeilko H. and De Witt Hamer, Philip C. and Solheim, Ole and Reinertsen, Ingerid},
    journal={Frontiers in Neurology},
    volume={13},
    year={2022},
    url={https://www.frontiersin.org/articles/10.3389/fneur.2022.932219},
    doi={10.3389/fneur.2022.932219},
    issn={1664-2295}
}
```
