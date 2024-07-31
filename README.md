# Documentación del Proyecto

## Índice
- [ParticipantesController](#participantescontroller)
- [ProcesoElectoralController](#procesoelectoralcontroller)
- [Estilos CSS](#estilos-css)
- [JavaScript Principal](#javascript-principal)
- [JavaScript de Participantes](#javascript-de-participantes)
- [Página de Participantes](#pagina-de-participantes)
- [Configuración de la Aplicación Flask](#configuracion-de-la-aplicacion-flask)
- [Archivo Principal](#archivo-principal)

---

## ParticipantesController

### 1. Nombres Descriptivos
Se utilizaron nombres claros y descriptivos para los métodos en el controlador de participantes. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```python
@participantes_bp.route('/participantes', methods=['GET'])
def obtener_participantes(self):
    participantes = self.servicio.obtener_todos()
    return jsonify(participantes)
```

## ProcesoElectoralController

### 1. Nombres Descriptivos
Se utilizaron nombres claros y descriptivos para los métodos en el controlador de procesos electorales. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```python
@proceso_electoral_bp.route('/procesos-electorales', methods=['GET'])
def obtener_procesos(self):
    procesos = self.servicio.obtener_todos()
    return jsonify(procesos)
```

## Estilos CSS

### 1. Nombres Descriptivos
Se utilizaron nombres claros y descriptivos para las variables CSS. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```css
:root {
    --primary-color: #007bff;
    --primary-color-hover: #0056b3;
    --background-color: #f8f9fa;
    --text-color: #343a40;
    --border-color: #dee2e6;
    --white-color: #ffffff;
}
```

### 2. Comentarios
Se añadieron comentarios para describir las secciones del código CSS. Esto ayuda a otros desarrolladores a entender rápidamente la funcionalidad del código.

**Ejemplo:**
```css
/* Variables de diseño */
:root {
    --max-width-container: 800px;
    --padding-container: 20px;
}
```

## JavaScript Principal

### 1. Nombres Descriptivos
Se utilizó un mensaje claro en el console.log para indicar que el documento está completamente cargado y listo.

**Ejemplo:**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    console.log("Documento cargado y listo.");
});
```

## JavaScript de Participantes

### 1. Nombres Descriptivos
Se utilizaron nombres claros y descriptivos para variables y funciones. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```javascript
const listaParticipantes = document.getElementById('lista-participantes');
```

### 2. Comentarios
Se añadieron comentarios para describir la funcionalidad del código JavaScript. Esto ayuda a otros desarrolladores a entender rápidamente la estructura y propósito del código.

**Ejemplo:**
```javascript
// Obtener y mostrar la lista de participantes
fetch('/participantes')
    .then(response => response.json())
    .then(data => {
        data.forEach(participante => {
            const item = document.createElement('li');
            item.textContent = participante.nombre;
            listaParticipantes.appendChild(item);
        });
    });

```

## Página de Participantes

### 1. Estructura y Comentarios
Se añadieron comentarios para describir las secciones del código HTML. Esto ayuda a otros desarrolladores a entender rápidamente la estructura de la página.

**Ejemplo:**
```html
<!-- Lista para mostrar los participantes -->
<ul id="lista-participantes"></ul>
```

## Configuración de la Aplicación Flask

### 1. Comentarios y Docstrings
Se añadió un docstring a la función create_app para describir su propósito y lo que devuelve. Esto ayuda a otros desarrolladores a entender rápidamente la función de esta configuración.

**Ejemplo:**
```python
def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.
    
    Returns:
        app (Flask): La instancia de la aplicación Flask configurada.
    """
    app = Flask(__name__)
    # Registro de Blueprints
    app.register_blueprint(participantes_bp)
    app.register_blueprint(proceso_electoral_bp)
    
    return app
```

## Archivo Principal

### 1. Comentarios
Se añadieron comentarios para describir el propósito del código, como la creación de la instancia de la aplicación y la ejecución en modo de depuración. Esto ayuda a otros desarrolladores a entender rápidamente el propósito de cada parte del código.

**Ejemplo:**
```python
# Crear una instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)
```

## Principios SOLID en ParticipantesController

### 1. Principio de Responsabilidad Única (SRP)
El ParticipantesController tiene una única responsabilidad: manejar las solicitudes relacionadas con los participantes. No mezcla lógica de negocio ni de acceso a datos.

**Ejemplo:**
```python
class ParticipantesController:
    def __init__(self):
        self.servicio = ParticipantesServicio()

    @participantes_bp.route('/participantes', methods=['GET'])
    def obtener_participantes(self):
        participantes = self.servicio.obtener_todos()
        return jsonify(participantes)

    @participantes_bp.route('/participantes', methods=['POST'])
    def crear_participante(self):
        data = request.json
        nuevo_participante = self.servicio.crear(data)
        return jsonify(nuevo_participante), 201

    @participantes_bp.route('/participantes/<int:id>', methods=['PUT'])
    def actualizar_participante(self, id):
        data = request.json
        participante_actualizado = self.servicio.actualizar(id, data)
        return jsonify(participante_actualizado)

    @participantes_bp.route('/participantes/<int:id>', methods=['DELETE'])
    def eliminar_participante(self, id):
        self.servicio.eliminar(id)
        return '', 204
```

### 2. Principio de Inversión de Dependencias (DIP)
El controlador depende de una abstracción (ParticipantesServicio) en lugar de una implementación concreta. Esto permite cambiar la implementación del servicio sin modificar el controlador.

**Ejemplo:**
```python
class ParticipantesController:
    def __init__(self, servicio):
        self.servicio = servicio

# Uso
servicio = ParticipantesServicio()
controller = ParticipantesController(servicio)
```

### 3. Principio de Abierto/Cerrado (OCP)
El ParticipantesController está abierto para la extensión (puedes añadir nuevos endpoints) pero cerrado para la modificación (no necesitas modificar el código existente para añadir nuevas funcionalidades).

**Ejemplo:**
```python
class ParticipantesController:
    # Métodos existentes...

    @participantes_bp.route('/participantes/<int:id>/detalle', methods=['GET'])
    def obtener_detalle_participante(self, id):
        detalle = self.servicio.obtener_detalle(id)
        return jsonify(detalle)
```

## Principios SOLID en ProcesoElectoralController

### 1. Principio de Responsabilidad Única (SRP)
El ProcesoElectoralController tiene una única responsabilidad: manejar las solicitudes relacionadas con los procesos electorales.

**Ejemplo:**
```python
class ProcesoElectoralController:
    def __init__(self):
        self.servicio = ProcesoElectoralServicio()

    @proceso_electoral_bp.route('/procesos-electorales', methods=['GET'])
    def obtener_procesos(self):
        procesos = self.servicio.obtener_todos()
        return jsonify(procesos)

    @proceso_electoral_bp.route('/procesos-electorales', methods=['POST'])
    def crear_proceso(self):
        data = request.json
        nuevo_proceso = self.servicio.crear(data)
        return jsonify(nuevo_proceso), 201

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['PUT'])
    def actualizar_proceso(self, id):
        data = request.json
        proceso_actualizado = self.servicio.actualizar(id, data)
        return jsonify(proceso_actualizado)

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>', methods=['DELETE'])
    def eliminar_proceso(self, id):
        self.servicio.eliminar(id)
        return '', 204
```

### 2. Principio de Inversión de Dependencias (DIP)
El controlador depende de una abstracción (ProcesoElectoralServicio) en lugar de una implementación concreta.

**Ejemplo:**
```python
class ProcesoElectoralController:
    def __init__(self, servicio):
        self.servicio = servicio

# Uso
servicio = ProcesoElectoralServicio()
controller = ProcesoElectoralController(servicio)
```

### 3. Principio de Abierto/Cerrado (OCP)
El ProcesoElectoralController está abierto para la extensión pero cerrado para la modificación.

**Ejemplo:**
```python
class ProcesoElectoralController:
    # Métodos existentes...

    @proceso_electoral_bp.route('/procesos-electorales/<int:id>/detalle', methods=['GET'])
    def obtener_detalle_proceso(self, id):
        detalle = self.servicio.obtener_detalle(id)
        return jsonify(detalle)
```

## Principios de Estilo CSS Legible en estilos_generales.css

### 1. Principio de Responsabilidad Única (SRP)
Cada sección de estilos CSS tiene una responsabilidad única, por ejemplo, estilizar el cuerpo del documento, encabezados, listas y botones. No mezcla estilos de diferentes componentes.

**Ejemplo:**
```css
/* Estilo global del cuerpo */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: var(--background-color);
}

/* Estilo para los encabezados */
h1 {
    color: var(--text-color);
}

/* Estilo para listas no ordenadas */
ul {
    list-style-type: none;
    padding: 0;
}

/* Estilo para los elementos de la lista */
li {
    padding: 10px;
    background-color: var(--white-color);
    margin-bottom: 5px;
    border: 1px solid var(--border-color);
    border-radius: 5px;
}

/* Estilo para los botones */
button {
    background-color: var(--primary-color);
    color: var(--white-color);
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

/* Estilo para el estado hover de los botones */
button:hover {
    background-color: var(--primary-color-hover);
}
```

### 3. Principio de Abierto/Cerrado (OCP)
El archivo CSS está abierto para la extensión (puedes añadir nuevos estilos) pero cerrado para la modificación (no necesitas modificar el código existente para añadir nuevos estilos).

**Ejemplo:**
```css
/* Estilo para los párrafos */
p {
    color: var(--text-color);
    line-height: 1.6;
}
```

## JavaScript Principal

### 1. Principio de Responsabilidad Única (SRP)
Se utilizó un mensaje claro en el console.log para indicar que el documento está completamente cargado y listo.

**Ejemplo:**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    console.log("Documento cargado y listo.");
});
```

## JavaScript de Participantes

### 1. Principio de Responsabilidad Única (SRP)
Se utilizaron nombres claros y descriptivos para variables y funciones. Esto facilita la comprensión del código y su propósito.

**Ejemplo:**
```javascript
const listaParticipantes = document.getElementById('lista-participantes');

fetch('/participantes')
    .then(response => response.json())
    .then(data => {
        data.forEach(participante => {
            const item = document.createElement('li');
            item.textContent = participante.nombre;
            listaParticipantes.appendChild(item);
        });
    });

// Evento para agregar participante (suponiendo que tienes un formulario)
const form = document.getElementById('form-participante');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    const nombre = document.getElementById('nombre').value;

    fetch('/participantes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre: nombre })
    })
    .then(response => response.json())
    .then(participante => {
        const item = document.createElement('li');
        item.textContent = participante.nombre;
        listaParticipantes.appendChild(item);
        form.reset();
    });
});
```

## Página de Participantes

### 1. Principio de Responsabilidad Única (SRP)
Se añadieron comentarios para describir las secciones del código HTML. Esto ayuda a otros desarrolladores a entender rápidamente la estructura de la página.

**Ejemplo:**
```html
<!-- Lista para mostrar los participantes -->
<ul id="lista-participantes"></ul>
```

## Configuración de la Aplicación Flask

### 1. Principio de Responsabilidad Única (SRP)
La función create_app tiene una única responsabilidad: crear y configurar una instancia de la aplicación Flask.

**Ejemplo:**
```python
def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.
    
    Returns:
        app (Flask): La instancia de la aplicación Flask configurada.
    """
    app = Flask(__name__)
    # Registro de Blueprints
    app.register_blueprint(participantes_bp)
    app.register_blueprint(proceso_electoral_bp)
    
    return app
```

## Archivo Principal

### 1. Principio de Responsabilidad Única (SRP)
Se añadieron comentarios para describir el propósito del código, como la creación de la instancia de la aplicación y la ejecución en modo de depuración. Esto ayuda a otros desarrolladores a entender rápidamente el propósito de cada parte del código.

**Ejemplo:**
```python
# Crear una instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)
```
