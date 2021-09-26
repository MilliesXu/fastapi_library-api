from sqlmodel import Field, SQLModel
from typing import Optional

class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
