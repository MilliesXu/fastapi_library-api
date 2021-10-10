from fastapi import FastAPI
from config.Database import Database

from routers import user, authentification


db = Database()
db.create_db_and_tables()

app = FastAPI()

app.include_router(user.router)
app.include_router(authentification.router)
