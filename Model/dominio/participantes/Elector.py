from flask import Flask, request, jsonify

app = Flask(__name__)

class Elector:
    def __init__(self, id, correo, contraseña, nombre, apellido):
        self.id = id
        self.correo = correo
        self.contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.ha_votado = False

    def registrar(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        return "Registro exitoso"

    def iniciar_sesion(self, correo, contraseña):
        if self.correo == correo and self.contraseña == contraseña:
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

# Crear un ejemplo de elector y candidato
elector = Elector(id=1, correo="ejemplo@correo.com", contraseña="password123", nombre="Juan", apellido="Perez")
candidato = Candidato(id=2, correo="candidato@correo.com", contraseña="password123", nombre="Maria", apellido="Gomez", candidatura="Presidencial", propuesta="Mejora económica")

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    return jsonify({"mensaje": elector.registrar(nombre, apellido)})

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    data = request.json
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    return jsonify({"mensaje": elector.iniciar_sesion(correo, contraseña)})

@app.route('/votar', methods=['POST'])
def votar():
    return jsonify({"mensaje": elector.votar()})

@app.route('/estado_voto', methods=['GET'])
def estado_voto():
    return jsonify({"mensaje": elector.estado_voto()})

@app.route('/editar_datos', methods=['POST'])
def editar_datos():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    return jsonify({"mensaje": elector.editar_datos(nombre, apellido)})

@app.route('/modificar_propuesta', methods=['POST'])
def modificar_propuesta():
    data = request.json
    propuesta = data.get('propuesta')
    return jsonify({"mensaje": candidato.modificar_propuesta(propuesta)})

@app.route('/actualizar_perfil', methods=['POST'])
def actualizar_perfil():
    data = request.json
    candidatura = data.get('candidatura')
    propuesta = data.get('propuesta')
    return jsonify({"mensaje": candidato.actualizar_perfil(elector, candidatura, propuesta)})

@app.route('/registrar_candidato', methods=['POST'])
def registrar_candidato():
    data = request.json
    candidatura = data.get('candidatura')
    propuesta = data.get('propuesta')
    return jsonify({"mensaje": candidato.registrar_candidato(elector, candidatura, propuesta)})

if __name__ == '__main__':
    app.run(debug=True)
