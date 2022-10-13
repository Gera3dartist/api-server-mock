from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "ok"}


@app.get("/healthz")
async def root():
    return {"health": "GUT"}
