from Model.extensions import db
from sqlalchemy import Column, Integer, String, Boolean

class Candidato(db.Model):
    __tablename__ = 'candidato'
    id = Column(Integer, primary_key=True)
    candidatura = Column(String(255), nullable=False)
    propuesta = Column(String(255), nullable=False)