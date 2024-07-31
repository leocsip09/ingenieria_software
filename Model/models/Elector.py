from Model.extensions import db
from sqlalchemy import Column, Integer, String, Boolean

class Elector(db.Model):
    __tablename__ = 'elector'
    id = Column(Integer, primary_key=True)
    correo = Column(String(255), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    estado_voto = Column(Boolean, default=False)