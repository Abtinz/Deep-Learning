# MNIST GAN Generator

## Project Overview

MNIST GAN Generator is a focused project in this repository that explores digit generation experiments using baseline and convolutional GAN setups. The implementation is notebook/script oriented, so you can inspect each phase (setup, experimentation, and outputs) in a practical, reproducible workflow.

The project is designed as a learning-and-building artifact rather than just a final demo. That means the folder captures iterative reasoning, experimentation choices, and intermediate patterns that are useful for extending the work into larger systems.

## Project Files

- `GAN_Convolution.ipynb`

## Technologies Used

The technical stack used here includes Jupyter Notebook, Python, Deep learning framework, Image plotting utilities. These technologies were selected to keep the workflow modular: data/loading, model execution, and evaluation can each be changed independently without rewriting the whole project.

From an engineering perspective, this stack supports fast iteration and clear separation of concerns. It allows you to move between notebook exploration and script-style execution, which is useful when transitioning from prototyping to a more production-oriented layout.

## Models and Core Tools

The core model/tooling layer in this project is: Convolutional GAN (`GAN_Convolution.ipynb`), Baseline dense GAN (`generated_images/GANs_normal_network.ipynb`). This model/tool choice defines the project’s quality, speed, and behavior envelope, so most of the prompt/configuration decisions in the folder are tuned around it.

Conceptually, this layer is the engine of the project: it transforms raw inputs into task-specific outputs and determines what kind of reasoning or generation is possible. Understanding this layer deeply helps you decide where to tune parameters, where to add retrieval/tools, and where to switch to a different model family entirely.

## Requirements

- Python 3.10+
- Jupyter
- MNIST-accessible ML stack
- Optional GPU

## Running Steps

1. Run `GAN_Convolution.ipynb` for convolutional architecture results.
2. Run `generated_images/GANs_normal_network.ipynb` for baseline comparison.
3. Compare training behavior and output quality across both notebooks.
