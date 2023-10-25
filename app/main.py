from fastapi import FastAPI
from routes import aluno
import uvicorn
from db.database import Base, engine


def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()



app = FastAPI()
app.include_router(aluno.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=80, reload=True, host="0.0.0.0")









