from fastapi import status, HTTPException
from sqlalchemy.sql.expression import update
from utils.Hash import Hash
from service.Service import Service

import models
import schemas

class UserService(Service):
    def __init__(self) -> None:
        super(UserService, self).__init__()

    async def create(self, request: schemas.User):
        if await self._db.get_by_params(models.User, request.email):
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail='Email is already used')

        hash = Hash()

        new_user = models.User(
            name = request.name,
            email = request.email,
            password = hash.get_password_hash(request.password),
        )

        return await self._db.create(new_user)

    async def get_all(self):
        users = await self._db.get_all(models.User)

        if not users:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='users not found')

        return users

    async def get_one(self, id: int):
        user = await self._db.get_by_params(models.User, id)

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='user not found')

        return user

    async def update(self, id: int, request: schemas.EditUser):
        user =  await self._db.get_by_params(models.User, id)

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='User not found')

        if await self._db.get_by_params(models.User, request.email):
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail='Email is already used')

        update_user = models.User(
            id = user.id,
            name = request.name,
            email = request.email,
            password = user.password,
        )

        return await self._db.update(models.User, update_user, id)
