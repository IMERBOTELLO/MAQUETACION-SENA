from fastapi import FastAPI
from backend.routers.usuarios import router as usuarios_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Esta funcionando!!"}

app.include_router(usuarios_router)