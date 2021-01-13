from sqlalchemy import Boolean, String, Integer, Column
from sqlalchemy.orm import relationship
import sys
from core.api.database import Base

class Product(Base):
    __tablename__="product"

    #product_id: Column(Integer, primary_key=True, index=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    title= Column(String(200))
    description= Column(String(600))
    is_active= Column(Boolean, default=True)

class Category(Base):
    __tablename__="category"

    id = Column(Integer, primary_key=True, nullable=False)
    title=Column(String(200))