from fastapi import APIRouter
from .resources import resource_router
from .users import user_router
# TODO: resource should be under project

api_router = APIRouter()

api_router.include_router(user_router, tags=['users'], prefix='/users' )
api_router.include_router(resource_router, tags=['Resources'], prefix='/resources' )
