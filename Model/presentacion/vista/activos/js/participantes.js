// Archivo: presentacion/vista/activos/js/participantes.js

document.addEventListener('DOMContentLoaded', function() {
    // Seleccionar el elemento de la lista de participantes
    const listaParticipantes = document.getElementById('lista-participantes');

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

    // Evento para agregar un nuevo participante
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
            form.reset(); // Limpiar el formulario después de agregar el participante
        });
    });
});
