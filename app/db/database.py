from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_server = 'alunos_orm.mssql.somee.com'
db_name = 'alunos_orm'
db_user = 'gapino_SQLLogin_1'
db_password = 'xh2p1xlr2j'

connection_string = f"mssql+pyodbc://{db_user}:{db_password}@{db_server}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"
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