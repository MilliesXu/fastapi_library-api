from fastapi import APIRouter, status, HTTPException
from service.UserService import UserService

import schemas

router = APIRouter(
    prefix = '/user',
    tags = ['Users'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request: schemas.User):
    try:
        service = UserService()

        return await service.create(request)
    except Exception as ex:
        error_dict = ex.__dict__

        if len(error_dict) > 0:
            raise HTTPException(error_dict['status_code'], error_dict['detail'])
        else:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Something wrong in the server')