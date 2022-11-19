
from sqlalchemy.ext.asyncio import AsyncSession

from api_server_mock.models import UserCreate
from api_server_mock.db.mock_api_tables import users


# async def create_user(user: UserCreate, session):
#     result = await session.execute(users.insert().returning(*users.c), [user.dict()])
#     return result


async def list_users(session):
    result = await session.execute(users.select())
    return result.fetchall()

