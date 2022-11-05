from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from api_server_mock.settings import config


engine = create_async_engine(
    config['mock_api_server']['db']['DATABASE_URL'], 
    future=True, echo=True
    )

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def with_transaction():
    async with engine.begin() as conn:
        yield conn
