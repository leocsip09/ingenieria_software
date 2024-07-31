class Candidato(Elector):
    def __init__(self, id, correo, contraseña, nombre, apellido, candidatura, propuesta):
        super().__init__(id, correo, contraseña, nombre, apellido)
        self.candidatura = candidatura
        self.propuesta = propuesta

    def modificar_propuesta(self, propuesta):
        self.propuesta = propuesta
        return "Propuesta modificada exitosamente"

    def actualizar_perfil(self, elector, candidatura, propuesta):
        self.nombre = elector.nombre
        self.apellido = elector.apellido
        self.candidatura = candidatura
        self.propuesta = propuesta
        return "Perfil actualizado exitosamente"

    def registrar_candidato(self, elector, candidatura, propuesta):
        self.id = elector.id
        self.correo = elector.correo
        self.contraseña = elector.contraseña
        self.nombre = elector.nombre
        self.apellido = elector.apellido
        self.candidatura = candidatura
        self.propuesta = propuesta
        return "Candidato registrado exitosamente"
