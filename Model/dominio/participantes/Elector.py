from Model.repositorio.MySQL.elector_repositorio_impl import ElectorRepositorioImpl
from Model.models.Elector import ElectorModelo

class Elector:
    def __init__(self, id, correo, contrasenia, nombre, apellido):
        self.id = id
        self.correo = correo
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.apellido = apellido
        self.ha_votado = False

    def registrar(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        return "Registro exitoso"

    def iniciar_sesion(self, correo, contrasenia):
        if self.correo == correo and self.contrasenia == contrasenia:
            return "Inicio de sesión exitoso"
        else:
            return "Correo o contraseña incorrectos"

    def votar(self):
        if not self.ha_votado:
            self.ha_votado = True
            return "Voto registrado"
        else:
            return "Ya ha votado"

    def estado_voto(self):
        return "Ha votado" if self.ha_votado else "No ha votado"

    def editar_datos(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        return "Datos editados exitosamente"

    def guardar_en_db(self):
        elector_modelo = ElectorModelo(
            id=self.id,
            correo=self.correo,
            contrasena=self.contrasenia,
            nombre=self.nombre,
            apellido=self.apellido,
            estado_voto=self.ha_votado
        )
        return ElectorRepositorioImpl.agregar_elector(elector_modelo)

    def eliminar_de_db(self):
        elector_modelo = ElectorModelo.query.get(self.id)
        return ElectorRepositorioImpl.eliminar_elector(elector_modelo)

    @staticmethod
    def obtener_por_id(id):
        elector_modelo = ElectorRepositorioImpl.obtener_elector_por_id(id)
        if elector_modelo:
            return Elector(
                id=elector_modelo.id,
                correo=elector_modelo.correo,
                contrasenia=elector_modelo.contrasena,
                nombre=elector_modelo.nombre,
                apellido=elector_modelo.apellido
            )
        return None

    def actualizar_en_db(self, nuevo_correo, nueva_contrasena, nuevo_nombre, nuevo_apellido, nuevo_estado_voto):
        return ElectorRepositorioImpl.actualizar_elector(
            self.id, nuevo_correo, nueva_contrasena, nuevo_nombre, nuevo_apellido, nuevo_estado_voto
        )