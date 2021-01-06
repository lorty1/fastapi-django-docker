from product import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

products_test = [
    {
        'id':1,
        'title': 'Beajolais nouveau',
        'description': 'Vin blanc à boire en apéritif',
        'is_active': True
    },
        {
        'id':2,
        'title': 'Marin d\'eau douce',
        'description': 'Vin rouge à boire en apéritif',
        'is_active': False
    }
]
categories_test = [
    {
        'id':1,
        'title': 'Vin blanc',
    },
        {
        'id':2,
        'title': 'Vin rouge',
    }
]
for item in products_test:
    db_products = models.Product(
        id = item['id'],
        title = item['title'],
        description = item['description'],
        is_active = item['is_active']
    )
    db.add(db_products)
    


for item in categories_test:
    db_categories = models.Category(
        id = item['id'],
        title = item['title'],
    )
    db.add(db_categories)

db.commit()
db.close()