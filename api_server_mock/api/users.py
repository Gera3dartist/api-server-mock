
from fastapi import APIRouter, Depends
from api_server_mock.models import UserCreate
from api_server_mock.db.session import get_session, with_transaction;  
from api_server_mock.services import users


user_router = APIRouter()


@user_router.post("/")
async def register_user(user: UserCreate, session=Depends(with_transaction)):
    result = await users.create_user(user, session)
    print(f'>>>RESULT: {result}')
    return {"Status": "OK"}



@user_router.get("/")
async def register_user(session=Depends(with_transaction)):
    result = await users.list_users(session)
    print(f'>>>RESULT: {result}')
    return {"Result": list(result)}