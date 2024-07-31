# sistema de elecciones online 
# De qué trata? Un sistema online donde realizar las votaciones, con vision de elector y candidato
# Qué encontramos en el fork actual? Las clases de Elector y Candidato
# Tecnologias usadas: python flask
# Tareas Encargadas: crear la clase Elector y Candidato con python flask

# Ejemplo de crear clases: 
elector = Elector(id=1, correo="ejemplo@correo.com", contraseña="password123", nombre="Juan", apellido="Perez")
candidato = Candidato(id=2, correo="candidato@correo.com", contraseña="password123", nombre="Maria", apellido="Gomez",
candidatura="Presidencial", propuesta="Mejora económica")

# SOLID: Single responsability, Liskov y principio de abierto/cerrado
    //Single responsability Cada clase debe tener una única responsabilidad o motivo para cambiar. 
    class Elector:
    ... inicializacion ...
    def registrar(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        return "Registro exitoso"

        
    //Liskov Los objetos de una clase derivada deben poder sustituir a objetos de su clase base sin alterar el funcionamiento correcto del programa.
       class Candidato(Elector):
    def __init__(self, id, correo, contraseña, nombre, apellido, candidatura, propuesta):
        super().__init__(id, correo, contraseña, nombre, apellido)
        self.candidatura = candidatura
        self.propuesta = propuesta

    def modificar_propuesta(self, propuesta):
        self.propuesta = propuesta
        return "Propuesta modificada exitosamente"
# Estilos usados: Cookbook, trinity y lazy river
    //Lazy River flujo de datos sin interrupciones

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
    Prueba: 
        candidato = Candidato(id=2, correo="candidato@correo.com", contraseña="password123", nombre="Maria", apellido="Gomez", candidatura="Presidencial", propuesta="Mejora económica")
