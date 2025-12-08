// API Configuration
const API_BASE_URL = 'http://localhost:8000';

// DOM Elements
const generateForm = document.getElementById('generateForm');
const generateBtn = document.getElementById('generateBtn');
const resultSection = document.getElementById('resultSection');
const generatedImage = document.getElementById('generatedImage');
const imageInfo = document.getElementById('imageInfo');
const downloadBtn = document.getElementById('downloadBtn');
const generateAnotherBtn = document.getElementById('generateAnotherBtn');
const gallery = document.getElementById('gallery');
const refreshGalleryBtn = document.getElementById('refreshGalleryBtn');
const errorMessage = document.getElementById('errorMessage');

let currentImageId = null;

// Show error message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    setTimeout(() => {
        errorMessage.style.display = 'none';
    }, 5000);
}

// Generate image
async function generateImage(event) {
    event.preventDefault();
    
    const prompt = document.getElementById('prompt').value;
    const steps = parseInt(document.getElementById('steps').value);
    const guidance = parseFloat(document.getElementById('guidance').value);
    const width = parseInt(document.getElementById('width').value);
    const height = parseInt(document.getElementById('height').value);
    
    // Disable button and show loading
    generateBtn.disabled = true;
    generateBtn.querySelector('.btn-text').style.display = 'none';
    generateBtn.querySelector('.btn-loader').style.display = 'inline';
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                prompt,
                num_inference_steps: steps,
                guidance_scale: guidance,
                width,
                height
            })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to generate image');
        }
        
        const data = await response.json();
        currentImageId = data.id;
        
        // Display the generated image
        displayGeneratedImage(data);
        
        // Refresh gallery
        loadGallery();
        
    } catch (error) {
        console.error('Error generating image:', error);
        showError(`Error: ${error.message}`);
    } finally {
        // Re-enable button
        generateBtn.disabled = false;
        generateBtn.querySelector('.btn-text').style.display = 'inline';
        generateBtn.querySelector('.btn-loader').style.display = 'none';
    }
}

// Display generated image
function displayGeneratedImage(data) {
    generatedImage.src = `${API_BASE_URL}/api/image/${data.id}?t=${Date.now()}`;
    generatedImage.onload = () => {
        resultSection.style.display = 'block';
        resultSection.scrollIntoView({ behavior: 'smooth' });
    };
    
    imageInfo.innerHTML = `
        <strong>Prompt:</strong> ${data.prompt}<br>
        <strong>Model:</strong> ${data.model_name}<br>
        <strong>Created:</strong> ${new Date(data.created_at).toLocaleString()}
    `;
}

// Download image
async function downloadImage() {
    if (!currentImageId) return;
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/image/${currentImageId}`);
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `generated_image_${currentImageId}.png`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    } catch (error) {
        console.error('Error downloading image:', error);
        showError('Failed to download image');
    }
}

// Generate another image
function generateAnother() {
    resultSection.style.display = 'none';
    document.getElementById('prompt').focus();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Load gallery
async function loadGallery() {
    gallery.innerHTML = '<div class="loading">Loading gallery...</div>';
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/images?limit=20`);
        if (!response.ok) {
            throw new Error('Failed to load gallery');
        }
        
        const data = await response.json();
        
        if (data.images.length === 0) {
            gallery.innerHTML = `
                <div class="empty-gallery">
                    <div class="empty-gallery-icon">🖼️</div>
                    <p>No images yet. Generate your first image!</p>
                </div>
            `;
            return;
        }
        
        gallery.innerHTML = data.images.map(img => `
            <div class="gallery-item" onclick="viewImage(${img.id})">
                <img src="${API_BASE_URL}/api/image/${img.id}" alt="${img.prompt}">
                <div class="gallery-item-info">
                    <div class="prompt">${escapeHtml(img.prompt)}</div>
                    <div class="date">${new Date(img.created_at).toLocaleString()}</div>
                </div>
            </div>
        `).join('');
        
    } catch (error) {
        console.error('Error loading gallery:', error);
        gallery.innerHTML = '<div class="loading">Failed to load gallery</div>';
    }
}

// View image in detail
async function viewImage(imageId) {
    try {
        const response = await fetch(`${API_BASE_URL}/api/image/${imageId}/info`);
        if (!response.ok) {
            throw new Error('Failed to load image info');
        }
        
        const data = await response.json();
        currentImageId = data.id;
        displayGeneratedImage(data);
    } catch (error) {
        console.error('Error viewing image:', error);
        showError('Failed to load image');
    }
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Event Listeners
generateForm.addEventListener('submit', generateImage);
downloadBtn.addEventListener('click', downloadImage);
generateAnotherBtn.addEventListener('click', generateAnother);
refreshGalleryBtn.addEventListener('click', loadGallery);

// Load gallery on page load
loadGallery();

// Check API connection on load
fetch(`${API_BASE_URL}/`)
    .then(response => response.json())
    .then(data => {
        console.log('API connected:', data);
    })
    .catch(error => {
        console.error('API connection failed:', error);
        showError('Cannot connect to API. Make sure the server is running on http://localhost:8000');
    });

