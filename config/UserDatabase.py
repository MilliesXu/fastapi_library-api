from sqlmodel import Session, select
from config.Database import Database

class UserDatabase(Database):
    def __init__(self) -> None:
        super(UserDatabase, self).__init__()

    async def get_by_params(self, object: object, email: str):
        with Session(self._engine) as session:
            statement = select(object).where(object.email == email)

            return session.exec(statement).first()