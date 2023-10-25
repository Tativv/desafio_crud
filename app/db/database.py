from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_server = 'localhost'
db_name = 'desafio'
db_user = 'postgres'
db_password = '123'

connection_string = f"sqlite:///desafio.db"
engine = create_engine(connection_string, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()