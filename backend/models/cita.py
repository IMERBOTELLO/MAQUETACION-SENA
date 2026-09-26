from sqlalchemy import Column, Integer, String, Date, Enum, Time, ForeignKey
from backend.database.base import Base

class Cita(Base):
    __tablename__ = 'cita'
    
    id_cita = Column(Integer, primary_key = True, autoincrement = True)
    nombre_paciente = Column(String(100), nullable = False)
    numero_documento_paciente = Column(String(15), ForeignKey('paciente.numero_documento'), nullable = False)
    fecha = Column(Date, nullable = False)
    hora = Column(Time, nullable = False)
    servicio = Column(Enum('CARDIOLOGIA', 'PEDIATRIA', 'GINECOLOGIA', 'MEDICINA_INTERNA', 'CIRUGIA_GENERAL', 'ORTOPEDIA', 'TRAUMATOLOGIA', 'DERMATOLOGIA'), nullable = False)
    id_medico = Column(Integer, ForeignKey('medico.ID_MEDICO'), nullable = False)