import asyncpg
from fastapi import FastAPI
import logging 
logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI, config: dict):
    logger.info('Connecting to db')
    app.state.pool = await asyncpg.create_pool(
        user=config.mock_api_server.db.user,
        password=config.mock_api_server.db.password,
        port=config.mock_api_server.db.port,
        host=config.mock_api_server.db.host,
        database=config.mock_api_server.db.database,
        min_size=config.mock_api_server.db.min_connection_count,
        max_size=config.mock_api_server.db.max_connection_count,
    )
    logger.info('Connected to db')


async def close_db_connection(app: FastAPI, config: dict):
    logger.info('Clossing connections to db')
    await app.state.pool.close()
    logger.info('Connection closed')
