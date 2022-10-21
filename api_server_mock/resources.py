from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "ok"}


@app.get("/healthz")
async def healthz():
    return {"health": "GUT"}


@app.post("/register")
async def register():
    return {"health": "GUT"}
