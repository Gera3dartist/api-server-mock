
from api_server_mock.api.dependencies.database import get_repository
from api_server_mock.repositories.users import UsersRepository
from fastapi import APIRouter, Depends
from api_server_mock.models import UserCreate
from api_server_mock.db.session import with_transaction;  
from api_server_mock.services import users


user_router = APIRouter()


@user_router.post("/")
async def register_user(
    user: UserCreate, 
    user_repository: UsersRepository=Depends(get_repository(UsersRepository))):
    result = await user_repository.create_user(user.email, user.name)
    return {"Status": "OK"}


@user_router.get("/")
async def register_user(
    user_repository: UsersRepository=Depends(get_repository(UsersRepository))
):
    result = await user_repository.list_users()
    print(f'>>>RESULT: {result}')
    return {"Result": list(result)}