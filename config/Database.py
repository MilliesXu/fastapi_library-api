from sqlmodel import create_engine, SQLModel, Session, select
from dotenv import load_dotenv

import os

class Database:
    def __init__(self) -> None:
        load_dotenv('.env')
        self.__SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
        self._engine = create_engine(
            self.__SQLALCHEMY_DATABASE_URL,
            connect_args={
                'check_same_thread': False
            }
        )

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self._engine)

    async def create(self, object: object):
        with Session(self._engine) as session:
            session.add(object)

            session.commit()
            session.refresh(object)

            return object

    async def get_all(self, object: object):
        with Session(self._engine) as session:
            statement = select(object)

            return session.exec(statement).all()

    async def get_by_id(self, object: object, id: int):
        with Session(self._engine) as session:
            result = session.get(object, id)

            return result

    async def update(self, object: object, object_update: object, id: int):
        with Session(self._engine) as session:
            result = session.get(object, id)
            attributes = object_update.dict(exclude_unset=True)

            for attribute, value in attributes.items():
                setattr(result, attribute, value)

            session.add(result)
            session.commit()

            session.refresh(result)

            return result

    async def delete(self, object: object, id: int):
        with Session(self._engine) as session:
            result = session.get(object, id)

            session.delete(result)
            session.commit()

            return {"Detail": "Success Deleted"}
