from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from apps.product import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)





@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/products/", response_model=List[schemas.Product])
def show_products(db: Session = Depends(get_db)):
    print('rrtrt')
    products = db.query(models.Product).all()
    return products

@app.get("/products/{pk}/", response_model=schemas.Product)
def show_product(pk, db: Session = Depends(get_db)):
    print(pk)
    product = db.query(models.Product).filter(models.Product.id==pk).first()
    return product

@app.post(
    '/products/',
    response_model=schemas.ProductOut,
    response_description="Product data added into the database"
)
async def create_product(product: schemas.ProductOut):
    data = product
    print(data['title'], type(data))
    if not 'title' in product:
        raise HTTPException(status_code=418, detail="Title is required !")
    return product

@app.delete("/products/{pk}/")
def delete_product(pk, db: Session = Depends(get_db)):
    print('rtererer')
    product = db.query(models.Product).filter(models.Product.id==pk).delete()
    db.commit()
    return {'Status': 'done'}

@app.get("/categories/", response_model=List[schemas.Category])
def show_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories

@app.get("/categories/{pk}/", response_model=schemas.Category)
def show_category(pk, db: Session = Depends(get_db)):
    print(pk)
    category = db.query(models.Category).filter(models.Category.id==pk).first()
    return category