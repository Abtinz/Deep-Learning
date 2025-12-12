# Z-Image Generator 🚀

A simple and beautiful tool to generate stunning images using the **Z-Image-Turbo** model from Hugging Face. This project leverages the power of diffusion models to create high-quality, photorealistic images from text prompts in just a few steps.

<!-- ![Generated Image Example](not provided yet when i arrive home i wi pass it here)  -->

## ✨ Features

- ⚡ **Ultra-Fast Generation**: Powered by Z-Image-Turbo for sub-second inference on capable GPUs.
- 🎨 **High-Quality Output**: Produces photorealistic and creative images with excellent text rendering.
- 🔧 **Customizable Parameters**: Adjust height, width, steps, and more for tailored results.
- 🖥️ **Easy to Use**: Simple Python function with minimal setup.
- 🌐 **Bilingual Support**: Excels in English and Chinese text prompts.

## 📦 Installation

This project uses [uv](https://github.com/astral-sh/uv) for fast and reliable package management.

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone or navigate to the project directory**:
   ```bash
   cd /path/to/LLM-GANs-Projects/image
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```
   This will install `torch` and `diffusers` (from source) as specified in `pyproject.toml`.

## 🛠️ Troubleshooting

- **Out of Memory**: Reduce `height` and `width` or enable CPU offloading in the code.
- **Installation Issues**: Ensure uv is installed and run `uv sync` in the project directory.
- **Model Download**: The first run may take time to download the model (~12GB).

*Powered by [Hugging Face Diffusers](https://github.com/huggingface/diffusers) and [Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo).* ✨