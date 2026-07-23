from sqlalchemy import Column, Integer, String, Date, Enum
from backend.database.base import Base

class Laboratorio(Base):
    __tablename__ = 'LABORATORIO'    
    
    id_lab =    Column(Integer, primary_key = True, autoincrement = True)
    nombre_paciente = Column(String(100), nullable = False)
    numero_documento = Column(String(100), nullable = False)
    tipo_examen = Column(Enum('SANGRE', 'HORINA', 'COVID', 'RADIOGRAFIA'), nullable = False)
    fecha = Column(Date, nullable = False)
    resultado = Column(String(100), nullable = False)