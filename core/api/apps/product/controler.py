from fastapi import APIRouter, FastAPI, Depends, HTTPException
from fastapi.exceptions import RequestValidationError
from apps.product import models, schemas
from typing import List
from database import engine, get_db
from sqlalchemy.orm import Session

router = APIRouter()
models.Base.metadata.create_all(bind=engine)



# -- Product CRUD --
@router.get("/products/", response_model=List[schemas.Product])
async def show_products(db: Session = Depends(get_db)):
    '''Return Product List'''
    products = db.query(models.Product).all()
    return products

@router.get("/products/{pk}/", response_model=schemas.Product)
async def show_product(pk: int, db: Session = Depends(get_db)):
    '''Take id an argument => Return Product object'''
    product = db.query(models.Product).filter(models.Product.id==pk).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produit non disponible !")
    return product


@router.post('/products/',
    response_model=schemas.ProductOut,
    response_description="Product data added into the database"
)
async def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    print(hasattr(product, 'title'))
    return product


@router.delete("/products/{pk}/")
async def delete_product(pk, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id==pk).delete()
    db.commit()
    return {'Status': 'done'}

# -- Category CRUD --
@router.get("/categories/", response_model=List[schemas.Category])
async def show_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories


@router.get("/categories/{pk}/", response_model=schemas.Category)
async def show_category(pk,db: Session = Depends(get_db)):
    print(pk)
    category = db.query(models.Category).filter(models.Category.id==pk).first()
    return category