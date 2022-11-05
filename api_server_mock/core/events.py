from fastapi import FastAPI

from api_server_mock.db.events import connect_to_db, close_db_connection


def create_start_app_handler(app: FastAPI, config: dict):
    async def start_app() -> None:
        await connect_to_db(app, config)
    return start_app


def create_stop_app_handler(app: FastAPI, config: dict):
    async def stop_app() -> None:
        await close_db_connection(app, config)
    return stop_app
