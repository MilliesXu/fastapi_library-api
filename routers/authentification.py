from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from service.AuthenticateService import AuthenticateService
from datetime import timedelta
from utils.Error import Error
from dotenv import load_dotenv
from config.Token import Token

import os
import models

router = APIRouter(
    prefix = '/token',
    tags = ['Login'],
)

@router.post("/", response_model=models.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        load_dotenv('.env')
        service = AuthenticateService()
        token = Token()
        user = await service.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = await token.create_access_token(
            data={"sub": user.email}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as ex:
        error = Error(ex)
        error.raise_error()