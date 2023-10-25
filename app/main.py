from fastapi import FastAPI
from app.routes import aluno
import pyodbc
import uvicorn
from app.db.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()



app = FastAPI()
app.include_router(aluno.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)









