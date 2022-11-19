import logging

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI, config: dict):
    print('Connecting to db')
    # app.state.engine = await asyncpg.create_pool(
    #     user=config.mock_api_server.db.user,
    #     password=config.mock_api_server.db.password,
    #     port=config.mock_api_server.db.port,
    #     host=config.mock_api_server.db.host,
    #     database=config.mock_api_server.db.database,
    #     min_size=config.mock_api_server.db.min_connection_count,
    #     max_size=config.mock_api_server.db.max_connection_count
        
    # )
    app.state.engine = create_async_engine(
        config['mock_api_server']['db']['DATABASE_URL'], 
        future=True, echo=True,
        # connect_args={"application_name":"mock-server"}
    )
    print('Connected to db')


async def close_db_connection(app: FastAPI, config: dict):
    logger.info('Clossing connections to db')
    await app.state.engine.dispose()
    logger.info('Connection closed')
