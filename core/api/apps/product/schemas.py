from pydantic import BaseModel
from typing import Optional, List

class Product(BaseModel):
    """
    Product table
    """
    id: Optional[int]
    title: str
    description: Optional[str] = None
    is_active: Optional[bool] = False

    class Config:
        orm_mode = True

class ProductOut(BaseModel):
    """
    Product table
    """
    title: str
    description: Optional[str] = None

class Category(BaseModel):
    """
    Category table
    """
    id: int
    title: str

    class Config:
        orm_mode = True