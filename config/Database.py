from sqlmodel import create_engine, SQLModel, Session, select

class Database:
    def __init__(self) -> None:
        self.__SQLALCHEMY_DATABASE_URL = 'sqlite:///./database.db'
        self.__engine = create_engine(
            self.__SQLALCHEMY_DATABASE_URL,
            connect_args={
                'check_same_thread': False
            }
        )

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.__engine)

    async def create(self, object: object):
        with Session(self.__engine) as session:
            session.add(object)

            session.commit()
            session.refresh(object)

            return object

    async def get_all(self, object: object):
        with Session(self.__engine) as session:
            statement = select(object)

            return session.exec(statement)

    async def get_by_id(self, object: object, id: int):
        with Session(self.__engine) as session:
            statement = select(object).where(object.id == id)

            return session.exec(statement).first()

    async def get_by_email(self, object: object, email: str):
        with Session(self.__engine) as session:
            statement = select(object).where(object.email == email)

            return session.exec(statement).first()

    async def update(self, object: object, object_update: object, id: int):
        with Session(self.__engine) as session:
            statement = select(object).where(object.id == id)

            result = session.exec(statement).one()
            attributes = object_update.__dict__

            for attribute, value in attributes:
                vars(result)[attribute] = value

            session.add(result)
            session.commit()

            session.refresh(result)

            return result

    async def delete(self, object: object, id: int):
        with Session(self.__engine) as session:
            statement = select(object).where(object.id == id)

            result = session.exec(statement).one()

            session.delete(result)
