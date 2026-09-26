from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from backend.database.base import Base

class Laboratorio(Base):
    __tablename__ = 'laboratorio'
    
    id_lab =    Column(Integer, ForeignKey('atencion_medica.ID_ATENCION'), primary_key=True, autoincrement=True)
    nombre_paciente = Column(String(100), nullable = False)
    numero_documento = Column(String(100), nullable = False)
    tipo_examen = Column(Enum('HEMOGRAMA_COMPLETO', 'GLICEMIA', 'PERFIL_LIPIDICO', 'RADIOGRAFIA_DE_TORAX', 'ECOGRAFIA_ABDOMINAL', 'PRUEBA_DE_ESFUERZO', 'BIOMETRIA_HEMATICA', 'EXAMEN_DE_ORINA'), nullable = False)
    fecha = Column(Date, nullable = False)
    resultado = Column(String(100), nullable = False)