from flask import Flask, render_template, request, redirect, url_for, flash
from Model.extensions import db

users = {
    'admin': 'password123'
}

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from .models import Candidato, Elector, eleccion, registro_electoral, administrador_eleccion
        db.create_all()

    # Aquí se definen las rutas
    @app.route('/')
    def logpage():
        return render_template('login.html')

    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/', methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            print('Inicio de sesión exitoso')
            return redirect(url_for('index'))
        else:
            print('Nombre de usuario o contraseña incorrectos')
            return redirect(url_for('logpage'))

    @app.route('/eleccion')
    def eleccion():
        return render_template('eleccion.html')

    @app.route('/registrar_candidato')
    def registrar_candidato():
        return render_template('registrar_candidato.html')

    @app.route('/registrar_elector')
    def registrar_elector():
        return render_template('registrar_elector.html')

    @app.route('/registro_electoral')
    def registro_electoral():
        return render_template('registro_electoral.html')

    @app.route('/resultados')
    def resultados():
        return render_template('resultados.html')

    @app.route('/modificar_perfil')
    def modificar_perfil():
        return render_template('modificar_perfil.html')

    @app.route('/administrador_eleccion')
    def administrador_eleccion():
        return render_template('administrador_eleccion.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
