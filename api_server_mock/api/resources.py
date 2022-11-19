from fastapi import APIRouter

resource_router = APIRouter()


@resource_router.post("/")
async def root():
    return {"message": "ok"}


@resource_router.get("/healthz")
async def healthz():
    return {"health": "GUT"}

