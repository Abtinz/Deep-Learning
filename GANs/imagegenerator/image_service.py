"""
Image generation service using HuggingFace models
"""
import os
import uuid
from datetime import datetime
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
from typing import Dict, Optional
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Configuration
IMAGES_DIR = "generated_images"
MODEL_NAME = "runwayml/stable-diffusion-v1-5"  # You can change this to other models
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Create images directory if it doesn't exist
os.makedirs(IMAGES_DIR, exist_ok=True)

# Thread pool for running model inference
executor = ThreadPoolExecutor(max_workers=1)


class ImageGeneratorService:
    """Service for generating images from text prompts"""
    
    def __init__(self):
        """Initialize the image generator service"""
        self.model_name = MODEL_NAME
        self.device = DEVICE
        self.pipeline = None
        self._load_model()
    
    def _load_model(self):
        """Load the Stable Diffusion model"""
        print(f"Loading model {self.model_name} on device {self.device}...")
        try:
            # Load the pipeline
            self.pipeline = StableDiffusionPipeline.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                safety_checker=None,  # Disable safety checker for faster generation
                requires_safety_checker=False
            )
            self.pipeline = self.pipeline.to(self.device)
            
            # Enable memory efficient attention if available
            if hasattr(self.pipeline, "enable_attention_slicing"):
                self.pipeline.enable_attention_slicing()
            
            print(f"Model loaded successfully on {self.device}")
        except Exception as e:
            print(f"Error loading model: {e}")
            print("Falling back to CPU...")
            self.device = "cpu"
            self.pipeline = StableDiffusionPipeline.from_pretrained(
                self.model_name,
                torch_dtype=torch.float32
            )
            self.pipeline = self.pipeline.to(self.device)
    
    def _generate_image_sync(
        self,
        prompt: str,
        num_inference_steps: int = 20,
        guidance_scale: float = 7.5,
        width: int = 512,
        height: int = 512
    ) -> Image.Image:
        """Synchronous image generation (runs in thread pool)"""
        if self.pipeline is None:
            raise RuntimeError("Model not loaded")
        
        # Generate image
        image = self.pipeline(
            prompt=prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            width=width,
            height=height
        ).images[0]
        
        return image
    
    async def generate_image(
        self,
        prompt: str,
        num_inference_steps: int = 20,
        guidance_scale: float = 7.5,
        width: int = 512,
        height: int = 512
    ) -> Dict[str, str]:
        """
        Generate an image from a text prompt
        
        Args:
            prompt: Text prompt for image generation
            num_inference_steps: Number of inference steps
            guidance_scale: Guidance scale for generation
            width: Image width
            height: Image height
        
        Returns:
            Dictionary with image_path and model_name
        """
        # Run generation in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        image = await loop.run_in_executor(
            executor,
            self._generate_image_sync,
            prompt,
            num_inference_steps,
            guidance_scale,
            width,
            height
        )
        
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        filename = f"image_{timestamp}_{unique_id}.png"
        image_path = os.path.join(IMAGES_DIR, filename)
        
        # Save image
        image.save(image_path)
        
        return {
            "image_path": image_path,
            "model_name": self.model_name
        }


# Alternative: Using HuggingFace Inference API (no local model loading)
class HuggingFaceAPIImageService:
    """Service using HuggingFace Inference API (requires API key)"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize with HuggingFace API
        
        Args:
            api_key: HuggingFace API key (optional, can use environment variable)
        """
        self.api_key = api_key or os.getenv("HUGGINGFACE_API_KEY")
        self.model_name = "runwayml/stable-diffusion-v1-5"
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
    
    async def generate_image(
        self,
        prompt: str,
        num_inference_steps: int = 20,
        guidance_scale: float = 7.5,
        width: int = 512,
        height: int = 512
    ) -> Dict[str, str]:
        """
        Generate image using HuggingFace Inference API
        
        Note: This requires a HuggingFace API key and internet connection
        """
        import aiohttp
        
        if not self.api_key:
            raise ValueError("HuggingFace API key is required")
        
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "inputs": prompt,
            "parameters": {
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
                "width": width,
                "height": height
            }
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_url, headers=headers, json=payload) as response:
                if response.status == 200:
                    image_data = await response.read()
                    
                    # Save image
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    unique_id = str(uuid.uuid4())[:8]
                    filename = f"image_{timestamp}_{unique_id}.png"
                    image_path = os.path.join(IMAGES_DIR, filename)
                    
                    with open(image_path, "wb") as f:
                        f.write(image_data)
                    
                    return {
                        "image_path": image_path,
                        "model_name": f"{self.model_name} (API)"
                    }
                else:
                    error_text = await response.text()
                    raise RuntimeError(f"API error: {response.status} - {error_text}")

