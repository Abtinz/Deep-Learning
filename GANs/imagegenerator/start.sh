#!/bin/bash

# Start Image Generator - Backend + Frontend Together
# This script starts the FastAPI server which serves both the API and frontend

echo "=========================================="
echo "🚀 Starting Image Generator Application"
echo "=========================================="
echo ""
echo "Backend API: http://localhost:8000/api"
echo "Frontend UI: http://localhost:8000"
echo "API Docs:    http://localhost:8000/docs"
echo ""
echo "⏳ Starting server..."
echo "   (First run may take 5-15 minutes to download model)"
echo ""

cd "$(dirname "$0")"

# Start the server
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

