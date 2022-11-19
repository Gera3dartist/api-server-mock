from lib2to3.pytree import Base
from asyncpg import Connection
from asyncpg.pool import Pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
import typing as t

from fastapi import Depends
from starlette.requests import Request
from api_server_mock.repositories.base import BaseRespository


def _get_db_engine(request: Request) -> Pool:
    return request.app.state.engine


async def _get_connection_from_pool(
    engine: AsyncEngine = Depends(_get_db_engine)
) -> t.AsyncGenerator[Connection, None]:
    async with engine.begin() as conn:
        yield conn


def get_repository(
    repo_class: t.Type[BaseRespository]
) -> t.Callable[[Connection], BaseRespository]:
    def _get_repo(
        conn: Connection =  Depends(_get_connection_from_pool)
    ) -> BaseRespository:
        return repo_class(conn)
    return _get_repo
