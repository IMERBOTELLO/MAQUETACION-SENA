from fastapi import FastAPI
from backend.routers.usuarios import router as usuarios_router
from backend.routers import auth
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
def login():
    return FileResponse("frontend/html/login.html")

app.include_router(usuarios_router)

app.include_router(auth.router)