"""Main FastAPI application entry point."""
from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Items API",
    description="Simple API for managing items with SQLite database",
    version="1.0.0"
)

# Include routes
app.include_router(router)


@app.get("/")
def root():
    """Root endpoint."""
    return {
        "message": "Items API is running",
        "docs": "/docs",
        "endpoints": {
            "GET /items": "Get all items",
            "POST /items": "Create one or more items"
        }
    }

