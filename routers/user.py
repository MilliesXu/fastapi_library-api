from service.Service import Service
from fastapi import APIRouter, status, HTTPException
from service.UserService import UserService
from utils.Errror import Error

import models

router = APIRouter(
    prefix = '/user',
    tags = ['Users'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request: models.UserCreate):
    try:
        service = UserService()

        return await service.create(request)
    except Exception as ex:
        error = Error(ex)
        error.raise_error()

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[models.UserShow])
async def get_all_user():
    try:
        service = UserService()

        return await service.get_all()
    except Exception as ex:
        error = Error(ex)
        error.raise_error()

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=models.UserShow)
async def get_user(id: int):
    try:
        service = UserService()

        return await service.get_one(id)
    except Exception as ex:
        error = Error(ex)
        error.raise_error()

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=models.UserBase)
async def update_user(id: int, request: models.UserBase):
    try:
        service = UserService()

        return await service.update(id, request)
    except Exception as ex:
        error = Error(ex)
        error.raise_error()

@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_user(id: int):
    try:
        service = UserService()

        return await service.delete(id)
    except Exception as ex:
        error = Error(ex)
        error.raise_error()

