# TensorFlow Neural Network Track

## Project Overview

TensorFlow Neural Network Track is a focused project in this repository that explores foundational neural-network and CNN training workflows in TensorFlow/Keras. The implementation is notebook/script oriented, so you can inspect each phase (setup, experimentation, and outputs) in a practical, reproducible workflow.

The project is designed as a learning-and-building artifact rather than just a final demo. That means the folder captures iterative reasoning, experimentation choices, and intermediate patterns that are useful for extending the work into larger systems.

## Project Files

- `NeuralNetwork.ipynb`
- `from_scratch.ipynb`
- `keras_CNN.ipynb`

## Technologies Used

The technical stack used here includes TensorFlow, Keras, Jupyter Notebook, Python. These technologies were selected to keep the workflow modular: data/loading, model execution, and evaluation can each be changed independently without rewriting the whole project.

From an engineering perspective, this stack supports fast iteration and clear separation of concerns. It allows you to move between notebook exploration and script-style execution, which is useful when transitioning from prototyping to a more production-oriented layout.

## Models and Core Tools

The core model/tooling layer in this project is: Custom feed-forward and CNN architectures defined in notebooks. This model/tool choice defines the project’s quality, speed, and behavior envelope, so most of the prompt/configuration decisions in the folder are tuned around it.

Conceptually, this layer is the engine of the project: it transforms raw inputs into task-specific outputs and determines what kind of reasoning or generation is possible. Understanding this layer deeply helps you decide where to tune parameters, where to add retrieval/tools, and where to switch to a different model family entirely.

## Requirements

- Python 3.10+
- tensorflow
- keras
- numpy
- matplotlib
- jupyter

## Running Steps

1. Open each notebook (`NeuralNetwork.ipynb`, `from_scratch.ipynb`, `keras_CNN.ipynb`).
2. Run setup and data-loading cells.
3. Train/evaluate models and inspect metrics.
