"""API routes and endpoints."""
from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Item
from app.schemas import ItemIn, ItemOut

router = APIRouter()


@router.get("/items", response_model=List[ItemOut])
def read_items(db: Session = Depends(get_db)):
    """
    Get all items from database.
    
    Returns:
        List of all items
    """
    items = db.query(Item).all()
    return items


@router.post("/items", response_model=List[ItemOut], status_code=201)
def create_items(items: List[ItemIn], db: Session = Depends(get_db)):
    """
    Create one or more items.
    
    Args:
        items: List of items to create
        
    Returns:
        List of created items with their IDs
    """
    db_items = []
    
    for item_data in items:
        db_item = Item(
            name=item_data.name,
            price=float(item_data.price),
            created_at=item_data.created_at or datetime.utcnow()
        )
        db.add(db_item)
        db_items.append(db_item)
    
    db.commit()
    
    for db_item in db_items:
        db.refresh(db_item)
    
    return db_items

