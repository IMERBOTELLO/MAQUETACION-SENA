from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.dependencies import get_db
from backend.schemas.usuario_shema import UsuarioCreate, UsuarioResponse
from backend.services.usuario_service import crear_usuario

router = APIRouter(
    prefix = "/usuarios",
    tags = ["usuarios"]
)

@router.post("/", response_model = UsuarioResponse)
def crear(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return crear_usuario(db, usuario)
