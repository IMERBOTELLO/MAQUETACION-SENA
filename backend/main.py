from fastapi import FastAPI
from backend.routers.usuarios import router as usuarios_router
from backend.routers.resultados import router as resultados_router
from backend.routers.laboratorios import router as laboratorios_router
from backend.routers.atenciones_medicas import router as atenciones_router
from backend.routers.citas import router as citas_router
from backend.routers.medicos import router as medicos_router
from backend.routers import auth
from fastapi.staticfiles import StaticFiles
from backend.routers import vistas
from backend.routers.pacientes import router as pacientes_router

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# API
app.include_router(usuarios_router)
app.include_router(pacientes_router)
app.include_router(resultados_router)
app.include_router(laboratorios_router)
app.include_router(atenciones_router)
app.include_router(citas_router)
app.include_router(medicos_router)
app.include_router(auth.router)
app.include_router(vistas.router)
