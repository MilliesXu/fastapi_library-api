from sqlalchemy import sql
from sqlmodel import Field, SQLModel
from typing import Optional

class UserBase(SQLModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserShow(UserBase):
   id: Optional[int]

class User(UserCreate, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)

class UserResetPassword(SQLModel):
    password: str