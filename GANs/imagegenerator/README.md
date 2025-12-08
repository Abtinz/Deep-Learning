# Image Generator API

A simple FastAPI backend server for generating images from text prompts using HuggingFace Stable Diffusion models.

## Features

- 🎨 Text-to-image generation using Stable Diffusion models
- 💾 SQLite database for storing image metadata
- 📁 Local file storage for generated images
- 🔌 RESTful API with multiple endpoints
- 🚀 FastAPI with async support
- 🎯 Support for custom generation parameters

## Installation

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Set up environment (optional):**

If you want to use HuggingFace Inference API instead of local models, create a `.env` file:

```bash
HUGGINGFACE_API_KEY=your_api_key_here
```

## Usage

### Start the Server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### 1. Generate Image

**POST** `/api/generate`

Generate an image from a text prompt.

**Request Body:**
```json
{
  "prompt": "a beautiful sunset over mountains",
  "num_inference_steps": 20,
  "guidance_scale": 7.5,
  "width": 512,
  "height": 512
}
```

**Response:**
```json
{
  "id": 1,
  "prompt": "a beautiful sunset over mountains",
  "image_path": "generated_images/image_20231201_120000_abc123.png",
  "created_at": "2023-12-01T12:00:00",
  "model_name": "runwayml/stable-diffusion-v1-5"
}
```

### 2. Get Image

**GET** `/api/image/{image_id}`

Retrieve a generated image by ID. Returns the image file.

### 3. Get Image Info

**GET** `/api/image/{image_id}/info`

Get metadata about a generated image.

### 4. List Images

**GET** `/api/images?skip=0&limit=10`

List all generated images with pagination.

**Query Parameters:**
- `skip`: Number of records to skip (default: 0)
- `limit`: Maximum number of records to return (default: 10)

### 5. Delete Image

**DELETE** `/api/image/{image_id}`

Delete an image record and its file.

## Example Usage

### Using cURL

```bash
# Generate an image
curl -X POST "http://localhost:8000/api/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "a futuristic city at night with neon lights",
    "num_inference_steps": 25,
    "guidance_scale": 7.5
  }'

# List all images
curl "http://localhost:8000/api/images"

# Get image by ID
curl "http://localhost:8000/api/image/1" --output image.png
```

### Using Python

```python
import requests

# Generate an image
response = requests.post(
    "http://localhost:8000/api/generate",
    json={
        "prompt": "a beautiful landscape with mountains and lakes",
        "num_inference_steps": 20,
        "guidance_scale": 7.5
    }
)
result = response.json()
print(f"Image ID: {result['id']}")
print(f"Image Path: {result['image_path']}")

# Download the image
image_response = requests.get(f"http://localhost:8000/api/image/{result['id']}")
with open("downloaded_image.png", "wb") as f:
    f.write(image_response.content)
```

## Configuration

### Model Selection

You can change the model in `image_service.py`:

```python
MODEL_NAME = "runwayml/stable-diffusion-v1-5"  # Default
# Other options:
# "stabilityai/stable-diffusion-2-1"
# "CompVis/stable-diffusion-v1-4"
```

### Using HuggingFace API

If you prefer to use HuggingFace Inference API instead of loading models locally, modify `main.py`:

```python
from image_service import HuggingFaceAPIImageService

# Replace this line:
# image_service = ImageGeneratorService()

# With this:
image_service = HuggingFaceAPIImageService(api_key="your_api_key")
```

## Project Structure

```
imagegenerator/
├── main.py              # FastAPI application and endpoints
├── database.py          # Database models and setup
├── image_service.py     # Image generation service
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── data/               # SQLite database (created automatically)
└── generated_images/   # Generated images (created automatically)
```

## Requirements

- Python 3.8+
- CUDA-capable GPU (optional, but recommended for faster generation)
- ~10GB disk space for model files (first run will download the model)

## Notes

- The first run will download the Stable Diffusion model (~4GB), which may take some time
- Image generation on CPU can be slow (30-60 seconds per image)
- GPU acceleration significantly speeds up generation (5-10 seconds per image)
- Generated images are stored in the `generated_images/` directory
- Database is stored in `data/images.db`

## Troubleshooting

### Out of Memory Error

If you encounter CUDA out of memory errors:
1. Reduce image dimensions (width/height)
2. Use CPU instead of GPU
3. Use a smaller model

### Model Download Issues

If model download fails:
1. Check your internet connection
2. Try using HuggingFace API instead
3. Manually download the model from HuggingFace Hub

## License

This project uses models and code from various sources. Please check individual licenses:
- Stable Diffusion models: CreativeML Open RAIL-M License
- FastAPI: MIT License

