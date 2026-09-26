from sqlalchemy import Column, Integer, String, Date
from backend.database.base import Base

class Paciente(Base):
    __tablename__ = 'paciente'
    
    id_paciente = Column(Integer, primary_key = True, autoincrement = True)
    nombres_paciente = Column(String(255), nullable = False)
    apellidos_pacientes = Column(String(255), nullable = False)
    fecha_nacimiento = Column(Date, nullable = False)
    numero_documento = Column(String(25), nullable = False, unique = True)
    correo = Column(String(120), nullable = False, unique = True)
    fecha_registro = Column(Date, nullable = False)
    telefono = Column(String(20), nullable = False)