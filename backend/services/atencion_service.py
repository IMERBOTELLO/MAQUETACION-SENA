from sqlalchemy.orm import Session
from backend.models.atencion_medica import AtencionMedica
from backend.models.cita import Cita
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
    
def obtener_documento_para_laboratorio(db: Session, numero_documento: str):
    
    atencion = db.query(AtencionMedica).filter(
        AtencionMedica.numero_documento == numero_documento
    ).first()
    
    if atencion is None:
        return None
    
    # buscar cita
    
    cita = db.query(Cita).filter(
        Cita.numero_documento_paciente == numero_documento
    ).first()
    
    if cita is None:
        return None
    
    return {
        "id_atencion": atencion.id_atencion,
        "numero_documento": atencion.numero_documento,
        "nombre_paciente": cita.nombre_paciente,
    }
