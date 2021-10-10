from jose.exceptions import JWTError
from config.UserDatabase import UserDatabase
from utils.Hash import Hash
from service.Service import Service
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv
from jose import jwt
import models
import os


class AuthenticateService(Service):
    def __init__(self) -> None:
        super(AuthenticateService, self).__init__(UserDatabase)
        self.__hash = Hash()
        load_dotenv('.env')

    async def authenticate_user(self, username: str, password: str):
        user = await self._db.get_by_params(models.User, username)

        if not user:
            return False

        if not self.__hash.verify_password(password, user.password):
            return False
        
        return user
    
    async def get_current_user(self, token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, os.getenv('SECRETS'), algorithms=[os.getenv('ALGORITHM')])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = models.TokenData(username=username)
        except JWTError:
            raise credentials_exception

        user = await self._db.get_by_params(models.User, token_data.username)
        if user is None:
            raise credentials_exception

        return user

    async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user