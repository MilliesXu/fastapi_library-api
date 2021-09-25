from config.Database import Database
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
