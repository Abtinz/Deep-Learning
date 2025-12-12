import torch
from diffusers import ZImagePipeline
import PIL

def generate_image(
        prompt, 
        height=1024,
        width=1024, 
        num_inference_steps=9,
        guidance_scale=0.0,
        seed=42
    ) -> PIL.Image :
    """
    Generate an image using the Z-Image-Turbo model from Hugging Face.

    Args:
        prompt (str): The text prompt for image generation.
        height (int): Height of the generated image.
        width (int): Width of the generated image.
        num_inference_steps (int): Number of inference steps.
        guidance_scale (float): Guidance scale (set to 0.0 for Turbo models).
        seed (int): Random seed for reproducibility.

    Returns:
        PIL.Image: The generated image.
    """
    # Determine device and data type
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.bfloat16 if device == "cuda" else torch.float32

    # Load the pipeline with specified data type
    pipe = ZImagePipeline.from_pretrained(
        "Tongyi-MAI/Z-Image-Turbo",
        torch_dtype=dtype,
        low_cpu_mem_usage=False,
    ).to(device)

    # Optional: Enable CPU offloading for memory-constrained devices
    if device == "cpu":
        pipe.enable_model_cpu_offload()

    # Create generator
    generator = torch.Generator(device)\
        .manual_seed(seed)

    # Generate image
    image = pipe(
        prompt=prompt,
        height=height,
        width=width,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        generator=generator,
    ).images[0]

    return image

def save_image(image : PIL.Image, path: str):
    """
    Save the generated image to a file.

    Args:
        image (PIL.Image): The image to save.
        path (str): The file path to save the image.
    """

    image.save(path)
    print("Image saved as generated_image.png")

if __name__ == "__main__":
    prompt = "A beautiful landscape with mountains and a lake"
    saving_path = "generated_image.png"

    image = generate_image(
        prompt=prompt
    )

    save_image(
        image=image, 
        path=saving_path
    )