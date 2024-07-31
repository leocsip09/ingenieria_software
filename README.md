# Sistema de elecciones online 
## Error/Exception Handling
Este estilo se aplica en todos los métodos del repositorio para manejar posibles errores durante las operaciones con la base de datos. Si ocurre una excepción, la operación se revierte para mantener la integridad de los datos. 
## Cookbook
Con la integración de este estilo, se ve la implementación clara y directa de operaciones CRUD en los métodos del repositorio.

Error/Exception Handling y Cookbook se ven en:

*candidato_repositorio_impl.py:*
´´´python
class candidato_respositorio_impl:
    def agregar_candidato(self, candidato): # Create
        try:
            db.session.add(candidato)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def eliminar_candidato(self, candidato): # Delete
        try:
            db.session.delete(candidato)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def obtener_candidato_por_id(self, id): # Read
        try:
            candidato = Candidato.query.get(id)
            return candidato
        except Exception:
            return None

    def actualizar_candidato(self, id, nueva_candidatura, nueva_propuesta): # Update
        try:
            candidato = Candidato.query.get(id)
            if candidato:
                candidato.candidatura = nueva_candidatura
                candidato.propuesta = nueva_propuesta
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False
´´´
*elector_repositorio_impl.py:*
´´´python
class elector_repositorio_impl:
    def agregar_elector(self, elector):
        try:
            db.session.add(elector)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def eliminar_elector(self, elector):
        try:
            db.session.delete(elector)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    def obtener_elector_por_id(self, id):
        try:
            elector = Elector.query.get(id)
            return elector
        except Exception:
            return None
    
    def actualizar_elector(self, id, nuevo_correo, nueva_contrasena, nuevo_nombre, nuevo_apellido, nuevo_estado_voto):
        try:
            elector = Elector.query.get(id)
            if elector:
                elector.correo = nuevo_correo
                elector.contrasena = nueva_contrasena
                elector.nombre = nuevo_nombre
                elector.apellido = nuevo_apellido
                elector.estado_voto = nuevo_estado_voto
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False
´´´
## Persistent-Tables
Este estilo se aplica al definir los modelos de base de datos Candidato y Elector utilizando SQLAlchemy, lo que asegura que los datos se almacenan de manera óptima en la base de datos. 
Estas tablas se pueden ver en:

*En models/Candidato.py:*
´´´python
from Model.extensions import db

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidatura = db.Column(db.String(100), unique=True, nullable=False)
    propuesta = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Candidato {self.candidatura}>'
´´´
*En models/Elector.py:*
´´´python
from Model.extensions import db

class Elector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(120), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    estado_voto = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Elector {self.nombre} {self.apellido}>'
´´´
