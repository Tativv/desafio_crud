from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

db_server = 'dpg-cksln51f3gac73cehq9g-a.oregon-postgres.render.com'
db_name = 'desafio_3ecy'
db_user = 'desafio_3ecy_user'
db_password = 'VdueQ9CojBDOEyVN4HBsLO5KrhpBahGC'

connection_string = f"postgresql://${db_user}:${db_password}@${db_server}:5432/${db_name}"
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