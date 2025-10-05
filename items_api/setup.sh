#!/bin/bash
# Setup script for Items API

echo "🚀 Setting up Items API..."

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Test the installation
echo "✅ Testing installation..."
python -c "import fastapi; import uvicorn; import sqlalchemy; import pydantic; print('All dependencies installed successfully!')"

echo ""
echo "✨ Setup complete!"
echo ""
echo "To start the API:"
echo "  1. Activate venv: source venv/bin/activate"
echo "  2. Run: uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
echo "  3. Visit: http://localhost:8000/docs"
echo ""

