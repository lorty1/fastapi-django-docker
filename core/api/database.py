from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_api.db"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://will:Djibouti1788! \
# @db:3306/products_db"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://will:Djibouti1788! \
# @localhost:3306/products_db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


Base = declarative_base()
