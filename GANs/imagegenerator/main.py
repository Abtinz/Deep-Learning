"""
FastAPI Backend Server for Text-to-Image Generation
"""
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
import uvicorn
from datetime import datetime
import os

from database import init_db, get_db, ImageRecord
from image_service import ImageGeneratorService

# Initialize FastAPI app
app = FastAPI(
    title="Image Generator API",
    description="A simple API for generating images from text prompts using HuggingFace models",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_db()

# Initialize image generator service
image_service = ImageGeneratorService()

# Mount static files for frontend
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


# Request/Response Models
class GenerateImageRequest(BaseModel):
    prompt: str = Field(..., description="Text prompt for image generation", min_length=1, max_length=500)
    num_inference_steps: Optional[int] = Field(20, description="Number of inference steps", ge=10, le=50)
    guidance_scale: Optional[float] = Field(7.5, description="Guidance scale for generation", ge=1.0, le=20.0)
    width: Optional[int] = Field(512, description="Image width", ge=256, le=1024)
    height: Optional[int] = Field(512, description="Image height", ge=256, le=1024)


class ImageResponse(BaseModel):
    id: int
    prompt: str
    image_path: str
    created_at: str
    model_name: str


class ImageListResponse(BaseModel):
    images: List[ImageResponse]
    total: int


@app.get("/")
async def root():
    """Root endpoint - serve frontend or API info"""
    static_index = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(static_index):
        return FileResponse(static_index)
    return {
        "message": "Image Generator API",
        "version": "1.0.0",
        "endpoints": {
            "generate": "/api/generate",
            "get_image": "/api/image/{image_id}",
            "list_images": "/api/images",
            "delete_image": "/api/image/{image_id}"
        },
        "frontend": "/static/index.html"
    }


@app.post("/api/generate", response_model=ImageResponse)
async def generate_image(request: GenerateImageRequest, background_tasks: BackgroundTasks):
    """
    Generate an image from a text prompt
    
    Args:
        request: GenerateImageRequest with prompt and optional parameters
        background_tasks: FastAPI background tasks
    
    Returns:
        ImageResponse with image metadata
    """
    try:
        # Generate image
        result = await image_service.generate_image(
            prompt=request.prompt,
            num_inference_steps=request.num_inference_steps,
            guidance_scale=request.guidance_scale,
            width=request.width,
            height=request.height
        )
        
        # Save to database
        db = next(get_db())
        image_record = ImageRecord(
            prompt=request.prompt,
            image_path=result["image_path"],
            model_name=result["model_name"],
            created_at=datetime.now()
        )
        db.add(image_record)
        db.commit()
        db.refresh(image_record)
        
        return ImageResponse(
            id=image_record.id,
            prompt=image_record.prompt,
            image_path=image_record.image_path,
            created_at=image_record.created_at.isoformat(),
            model_name=image_record.model_name
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")


@app.get("/api/image/{image_id}")
async def get_image(image_id: int):
    """
    Retrieve a generated image by ID
    
    Args:
        image_id: ID of the image record
    
    Returns:
        Image file
    """
    db = next(get_db())
    image_record = db.query(ImageRecord).filter(ImageRecord.id == image_id).first()
    
    if not image_record:
        raise HTTPException(status_code=404, detail="Image not found")
    
    if not os.path.exists(image_record.image_path):
        raise HTTPException(status_code=404, detail="Image file not found")
    
    return FileResponse(
        image_record.image_path,
        media_type="image/png",
        filename=f"generated_image_{image_id}.png"
    )


@app.get("/api/images", response_model=ImageListResponse)
async def list_images(skip: int = 0, limit: int = 10):
    """
    List all generated images with pagination
    
    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
    
    Returns:
        List of image records
    """
    db = next(get_db())
    images = db.query(ImageRecord).order_by(ImageRecord.created_at.desc()).offset(skip).limit(limit).all()
    total = db.query(ImageRecord).count()
    
    return ImageListResponse(
        images=[
            ImageResponse(
                id=img.id,
                prompt=img.prompt,
                image_path=img.image_path,
                created_at=img.created_at.isoformat(),
                model_name=img.model_name
            )
            for img in images
        ],
        total=total
    )


@app.get("/api/image/{image_id}/info", response_model=ImageResponse)
async def get_image_info(image_id: int):
    """
    Get image metadata by ID
    
    Args:
        image_id: ID of the image record
    
    Returns:
        Image metadata
    """
    db = next(get_db())
    image_record = db.query(ImageRecord).filter(ImageRecord.id == image_id).first()
    
    if not image_record:
        raise HTTPException(status_code=404, detail="Image not found")
    
    return ImageResponse(
        id=image_record.id,
        prompt=image_record.prompt,
        image_path=image_record.image_path,
        created_at=image_record.created_at.isoformat(),
        model_name=image_record.model_name
    )


@app.delete("/api/image/{image_id}")
async def delete_image(image_id: int):
    """
    Delete an image record and file
    
    Args:
        image_id: ID of the image record
    
    Returns:
        Success message
    """
    db = next(get_db())
    image_record = db.query(ImageRecord).filter(ImageRecord.id == image_id).first()
    
    if not image_record:
        raise HTTPException(status_code=404, detail="Image not found")
    
    # Delete file if exists
    if os.path.exists(image_record.image_path):
        os.remove(image_record.image_path)
    
    # Delete record
    db.delete(image_record)
    db.commit()
    
    return {"message": "Image deleted successfully", "id": image_id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

