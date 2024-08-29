from fastapi import FastAPI
from database import sync_database, get_engine
from livros_controllers import router

app = FastAPI()

sync_database(get_engine())


app.include_router(router, prefix='/api/books')

