from fastapi import FastAPI
from config.Database import Database


db = Database()
db.create_db_and_tables()

app = FastAPI()
