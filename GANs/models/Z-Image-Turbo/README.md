# Z-Image-Turbo Project

## Project Overview

Z-Image-Turbo Project is a focused project in this repository that explores fast text-to-image generation with low-latency diffusion inference. The implementation is notebook/script oriented, so you can inspect each phase (setup, experimentation, and outputs) in a practical, reproducible workflow.

The project is designed as a learning-and-building artifact rather than just a final demo. That means the folder captures iterative reasoning, experimentation choices, and intermediate patterns that are useful for extending the work into larger systems.

## Project Files

- `image-generator.py`
- `main.py`
- `pyproject.toml`
- `requirements.txt`

## Technologies Used

The technical stack used here includes Python scripts, PyTorch, Diffusers ZImagePipeline. These technologies were selected to keep the workflow modular: data/loading, model execution, and evaluation can each be changed independently without rewriting the whole project.

From an engineering perspective, this stack supports fast iteration and clear separation of concerns. It allows you to move between notebook exploration and script-style execution, which is useful when transitioning from prototyping to a more production-oriented layout.

## Models and Core Tools

The core model/tooling layer in this project is: `Tongyi-MAI/Z-Image-Turbo`. This model/tool choice defines the project’s quality, speed, and behavior envelope, so most of the prompt/configuration decisions in the folder are tuned around it.

Conceptually, this layer is the engine of the project: it transforms raw inputs into task-specific outputs and determines what kind of reasoning or generation is possible. Understanding this layer deeply helps you decide where to tune parameters, where to add retrieval/tools, and where to switch to a different model family entirely.

## Requirements

- Python 3.10+
- torch
- diffusers
- Pillow
- GPU recommended

## Running Steps

1. Run `python image-generator.py` to generate and save an image.
2. Or integrate `generate_image(...)` from the module in your own script.
3. Adjust height/width/steps/guidance/seed for output control.
