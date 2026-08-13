from sqlalchemy import Column, Integer, String, Date, Enum, LargeBinary, ForeignKey
from backend.database.base import Base


class Resultado(Base):
    __tablename__ = 'RESULTADO'
    
    id_resultado = Column(Integer, primary_key = True, autoincrement = True)
    id_lab = Column(Integer, ForeignKey('LABORATORIO.id_lab'), nullable = False)
    documento_paciente = Column(String(30), nullable = False)
    nombre_paciente = Column(String(120), nullable = False)
    examen_medico = Column(
        Enum(
            'HEMOGRAMA_COMPLETO', 
            'GLICEMIA', 
            'PERFIL_LIPIDICO', 
            'RADIOGRAFIA_DE_TORAX', 
            'ECOGRAFIA_ABDOMINAL', 
            'PRUEBA_DE_ESFUERZO', 
            'BIOMETRIA_HEMATICA', 
            'EXAMEN_DE_ORINA'
        ),
    nullable = False)
    fecha_resultado = Column(Date, nullable = False)
    info_examen = Column(String(255), nullable = False)
    pdf = Column(LargeBinary, nullable = False)
    id_examen = Column(Integer, ForeignKey('atencion_medica.ID_ATENCION'), nullable = False)
    