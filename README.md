# MemoryMamba: Memory-Augmented State Space Model for Defect Recognition

This repository contains the code for the paper [MemoryMamba: Memory-Augmented State Space Model for Defect Recognition](https://arxiv.org/pdf/2405.03673) by Qianning Wang, He Hu, and Yucheng Zhou.

## Overview

MemoryMamba is a state-of-the-art framework for defect recognition using a state space model. This repository provides the implementation details and the necessary scripts to reproduce the results presented in the paper.

## Installation

To install the necessary dependencies, please use the following command:

```bash
pip install -r requirements.txt
```

## Demo

To run the model, use the following command:

```bash
python simple_memorymamba.py
```

## Dataset

The dataset used for training and evaluation is provided in [Huggingface](https://huggingface.co/datasets/MambaHub/MemoryMambaData).


## Citation

If you find this code useful, please consider citing our work:

```bibtex
@article{wang2024memorymamba,
  title={MemoryMamba: Memory-Augmented State Space Model for Defect Recognition},
  author={Wang, Qianning and Hu, He and Zhou, Yucheng},
  journal={arXiv preprint arXiv:2405.03673},
  year={2024}
}
```

## Acknowledgments

[VMamba](https://github.com/MzeroMiko/VMamba): the codebase we built upon.