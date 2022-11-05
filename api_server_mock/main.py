
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI

from api_server_mock.core.events import create_start_app_handler, create_stop_app_handler
from api_server_mock.api import api_router
from api_server_mock.settings import get_settings

def get_application() -> FastAPI:
    config = get_settings()
    application = FastAPI(**config['fastapi_kwargs'])
    # application.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=config['allowed_hosts'],
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )
    application.add_event_handler(
        "startup",
        create_start_app_handler(application, config)
    )
    

    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application, config)
    )

    # application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=config['api_prefix'])
    return application


app = get_application()
