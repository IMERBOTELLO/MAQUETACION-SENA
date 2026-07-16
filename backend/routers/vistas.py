from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()

# paginas html
@router.get("/")
def login():
    return FileResponse("frontend/html/login.html")

@router.get("/index")
def index():
    return FileResponse("frontend/html/index.html")

@router.get("/registro_paciente")
def registro_paciente():
    return FileResponse("frontend/html/registro_paciente.html")

@router.get("/consulta_pacientes")
def consulta_pacientes():
    return FileResponse("frontend/html/consulta_pacientes.html")

@router.get("/agendamientoDeCitas")
def agendamiento_de_citas():
    return FileResponse("frontend/html/agendamientoDeCitas.html")

@router.get("/confirmacionDeCitas")
def confirmacionDeCitas():
    return FileResponse("frontend/html/confirmacionDeCitas.html")

@router.get("/Medico")
def medico():
    return FileResponse("frontend/html/Medico.html")    

@router.get("/laboratorio")
def laboratorio():
    return FileResponse("frontend/html/laboratorio.html")

@router.get("/resultados")
def resultados():
    return FileResponse("frontend/html/resultados.html")