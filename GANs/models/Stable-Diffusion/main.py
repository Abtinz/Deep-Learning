import torch
from diffusers import DiffusionPipeline

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

MODEL_NAME = "stabilityai/stable-diffusion-xl-base-1.0"
IMAGE_OUTPUT_PATH_PREFIX= "stable-diffusion-generated-image-"
IMAGE_FORMAT = ".png"

pipe = DiffusionPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=dtype, 
    use_safetensors=True
    )

pipe.to(device)

prompt = input("Enter your prompt: ")

image = pipe(prompt).images[0]

PATH = IMAGE_OUTPUT_PATH_PREFIX + prompt.split(" ")[0] + IMAGE_FORMAT

image.save(PATH)     

