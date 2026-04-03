# GANs

This folder contains your generative image work, centered on GAN training workflows plus modern diffusion-style model experiments.

## What This Area Covers

- Generative Adversarial Networks (GANs): generator vs discriminator training for synthetic image creation.
- Image-model experimentation: prompt-to-image generation and editing with newer model families.
- Notebook-based prototyping for data prep, training loops, and output quality checks.

## Core Concepts Implemented

- Adversarial learning dynamics (generator/discriminator balance).
- Convolutional GAN architecture patterns.
- Progressive training ideas for higher-quality face synthesis.
- Text-to-image pipeline usage and model inference control (resolution, steps, guidance, seed).

## Projects In This Folder

- `Art-Portrate Generator`
  - `Art_Portraits_Generator.ipynb`
  - Portrait-generation workflow from dataset preparation to generated outputs.
- `Face Generation`
  - `(Progan)_Face_generation_with_GanAI_.ipynb`
  - Progressive GAN face-generation experiment.
- `MNIST generator`
  - `GAN_Convolution.ipynb`
  - `generated_images/GANs_normal_network.ipynb`
  - MNIST GAN baselines and convolutional variant comparisons.
- `models`
  - Stable Diffusion, Z-Image-Turbo, FLUX, and Imagen experiments.

## Models and Technologies Referenced

- `stabilityai/stable-diffusion-xl-base-1.0`
- `Tongyi-MAI/Z-Image-Turbo`
- `black-forest-labs/flux-1.1-pro`
- `black-forest-labs/flux-kontext-pro`
- `google/imagen-4`
- PyTorch
- Hugging Face Diffusers

