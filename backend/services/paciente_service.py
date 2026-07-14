from sqlalchemy.orm import Session
from backend.models.paciente import Paciente
from backend.schemas.paciente_shema import PacienteCreate

def crear_paciente(db: Session, paciente: PacienteCreate):

    nuevo_paciente = Paciente(
        nombres_paciente = paciente.nombres_paciente,
        apellidos_pacientes = paciente.apellidos_pacientes,
        fecha_nacimiento = paciente.fecha_nacimiento,
        numero_documento = paciente.numero_documento,
        correo = paciente.correo,
        fecha_registro = paciente.fecha_registro,
        telefono = paciente.telefono
    )

    db.add(nuevo_paciente)
    db.commit()
    db.refresh(nuevo_paciente)

    return nuevo_paciente


def obtener_pacientes(db: Session):
    return db.query(Paciente).all()


def obtener_paciente_por_id(db: Session, id_paciente: int):
    return db.query(Paciente).filter(
        Paciente.id_paciente == id_paciente
    ).first()


# NUEVA FUNCION
def obtener_paciente_por_documento(db: Session, numero_documento: str):
    return db.query(Paciente).filter(
        Paciente.numero_documento == numero_documento
    ).first()


def actualizar_paciente(db: Session, id_paciente: int, paciente: PacienteCreate):

    paciente_db = db.query(Paciente).filter(
        Paciente.id_paciente == id_paciente
    ).first()

    if paciente_db is None:
        return None

    paciente_db.nombres_paciente = paciente.nombres_paciente
    paciente_db.apellidos_pacientes = paciente.apellidos_pacientes
    paciente_db.fecha_nacimiento = paciente.fecha_nacimiento
    paciente_db.numero_documento = paciente.numero_documento
    paciente_db.correo = paciente.correo
    paciente_db.fecha_registro = paciente.fecha_registro
    paciente_db.telefono = paciente.telefono

    db.commit()
    db.refresh(paciente_db)

    return paciente_db


def eliminar_paciente(db: Session, id_paciente: int):

    paciente_db = db.query(Paciente).filter(
        Paciente.id_paciente == id_paciente
    ).first()

    if paciente_db is None:
        return None

    db.delete(paciente_db)
    db.commit()

    return paciente_db