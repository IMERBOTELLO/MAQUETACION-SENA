from sqlalchemy import Column, Integer, String, Date
from backend.database.base import Base


class AtencionMedica(Base):
    __tablename__ = "atencion_medica"

    id_atencion = Column("ID_ATENCION", Integer, primary_key=True, autoincrement=True)
    diagnostico = Column("DIAGNOSTICO", String(100), nullable=False)
    observaciones = Column("OBSERVACIONES", String(100), nullable=False)
    fecha_atencion = Column("FECHA_ATENCION", Date, nullable=False)
    numero_documento = Column("NUMERO_DOCUMENTO", String(20), nullable=False)
    examenes = Column("EXAMENES", String(255), nullable=False)