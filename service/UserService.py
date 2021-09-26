from fastapi import status, HTTPException
from config.Database import Database
from config.Hash import Hash
from service.Service import Service

import models
import schemas

class UserService(Service):
    async def create(self, request: schemas.User):
        if await self._db.get_by_email(models.User, request.email):
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail='Email is already used')

        hash = Hash()

        new_user = models.User(
            name = request.name,
            email = request.email,
            password = hash.get_password_hash(request.password),
        )

        return await self._db.create(new_user)