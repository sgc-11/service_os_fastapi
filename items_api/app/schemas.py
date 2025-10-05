"""Pydantic schemas for request/response validation."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, constr
from decimal import Decimal


class ItemIn(BaseModel):
    """Schema for creating items."""
    
    name: constr(min_length=1, max_length=200) = Field(
        ...,
        description="Item name",
        examples=["Lapiz"]
    )
    price: Decimal = Field(
        ...,
        gt=0,
        max_digits=10,
        decimal_places=2,
        description="Item price",
        examples=[1200.50]
    )
    created_at: Optional[datetime] = Field(
        None,
        description="Creation timestamp (optional)"
    )


class ItemOut(BaseModel):
    """Schema for returning items."""
    
    id: int
    name: str
    price: float
    created_at: datetime
    
    class Config:
        from_attributes = True

