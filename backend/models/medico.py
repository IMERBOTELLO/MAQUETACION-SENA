from sqlalchemy import Column, Integer, String
from backend.database.base import Base

class Medico(Base):
    __tablename__ = "medico"

    id_medico = Column("ID_MEDICO", Integer, primary_key=True, autoincrement=True)
    nombre_medico = Column("NOMBRE_MEDICO", String(100), nullable=False)
    especialidad = Column("ESPECIALIDAD", String(80), nullable=False)
    telefono = Column("TELEFONO", String(20), unique=True, nullable=False)
    correo = Column("CORREO", String(120), nullable=False)