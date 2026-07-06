from fastapi import FastAPI
from backend.routers.usuarios import router as usuarios_router
from backend.routers.medicos import router as medicos_router
from backend.routers import auth
from fastapi.staticfiles import StaticFiles
from backend.routers import vistas


app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# API
app.include_router(usuarios_router)
app.include_router(auth.router)
app.include_router(vistas.router)
app.include_router(medicos_router)