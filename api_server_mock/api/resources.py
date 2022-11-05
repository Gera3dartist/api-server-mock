from fastapi import APIRouter

resource_router = APIRouter()


@resource_router.get("/")
async def root():
    return {"message": "ok"}


@resource_router.get("/healthz")
async def healthz():
    return {"health": "GUT"}

