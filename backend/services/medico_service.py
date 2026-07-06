from sqlalchemy.orm import Session
from backend.models.medico import Medico
from backend.schemas.medico_shema import MedicoCreate


def crear_medico(db: Session, medico: MedicoCreate):
    nuevo_medico = Medico(
        nombre_medico=medico.nombre_medico,
        especialidad=medico.especialidad,
        telefono=medico.telefono,
        correo=medico.correo
    )

    db.add(nuevo_medico)
    db.commit()
    db.refresh(nuevo_medico)

    return nuevo_medico


def obtener_medicos(db: Session):
    return db.query(Medico).all()


def obtener_medico_por_id(db: Session, id_medico: int):
    return db.query(Medico).filter(
        Medico.id_medico == id_medico
    ).first()


def actualizar_medico(db: Session, id_medico: int, datos: MedicoCreate):

    medico = obtener_medico_por_id(db, id_medico)

    if medico is None:
        return None

    medico.nombre_medico = datos.nombre_medico
    medico.especialidad = datos.especialidad
    medico.telefono = datos.telefono
    medico.correo = datos.correo

    db.commit()
    db.refresh(medico)

    return medico


def eliminar_medico(db: Session, id_medico: int):

    medico = obtener_medico_por_id(db, id_medico)

    if medico is None:
        return None

    db.delete(medico)
    db.commit()

    return medico 