from config.Database import Database

class Service:
    def __init__(self, db: Database) -> None:
        self._db = db()

    async def create():
        pass

    async def get_all():
        pass

    async def get_one():
        pass

    async def update():
        pass

    async def delete():
        pass
