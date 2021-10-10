from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt

import os

class Token:
    def __init__(self) -> None:
        load_dotenv('.env')

    async def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, os.getenv('SECRETS'), algorithm=os.getenv('ALGORITHM'))
        return encoded_jwt
