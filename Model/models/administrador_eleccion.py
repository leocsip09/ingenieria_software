from Model.extensions import db

class Administrador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text)

    def __repr__(self):
        return f'<{self.nombre}'