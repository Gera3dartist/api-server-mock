from api_server_mock.db.mock_api_tables import users
from api_server_mock.models.domain.users import UserInDB
from .base import BaseRespository

class UsersRepository(BaseRespository):

    async def create_user(self, email: str, name: str) -> UserInDB:
        async with self.connection.transaction() as connection:
            user_row = await connection.execute(
                users.insert().returning(*users.c), 
                [dict(email=email, name=name)]
            )
            print(user_row)
            return UserInDB(**user_row)


    async def list_users(self):
        result = await self.connection.execute(users.select())
        return result.fetchall()

