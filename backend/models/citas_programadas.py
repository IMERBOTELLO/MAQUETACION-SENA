from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, UniqueConstraint
from backend.database.base import Base

class CitaProgramadas(Base):
    __tablename__ = 'CITAS_PROGRAMADAS'
    
    id_citas_programadas = Column(Integer, primary_key = True, autoincrement = True)
    documento = Column(String(15), ForeignKey('CITA.numero_documento_paciente'), nullable = False)
    nombre_paciente = Column(String(100), nullable = False)
    especialista = Column(String(100), nullable = False)
    fecha = Column(Date, nullable = False)
    hora = Column(Time, nullable = False)
    servicio = Column(String(100), nullable = False)