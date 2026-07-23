from sqlalchemy.orm import Session
from backend.models.atencion_medica import AtencionMedica
from backend.schemas.atencion_medica_shema import AtencionMedicaCreate


def crear_atencion(db: Session, atencion: AtencionMedicaCreate):
    nueva_atencion = AtencionMedica(**atencion.model_dump())
    db.add(nueva_atencion)
    db.commit()
    db.refresh(nueva_atencion)
    return nueva_atencion


def obtener_atenciones(db: Session):
    return db.query(AtencionMedica).all()


def obtener_atencion_por_id(db: Session, id_atencion: int):
    return db.query(AtencionMedica).filter(
        AtencionMedica.id_atencion == id_atencion
    ).first()
    
def obtener_atencion_por_numero_documento(db: Session, documento: str):
    return db.query(AtencionMedica).filter(
        AtencionMedica.numero_documento == documento
    ).first()
    
