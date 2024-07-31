# sistema de elecciones online 
# De qué trata? Un sistema online donde realizar las votaciones, con vision de elector y candidato
# Qué encontramos en el fork actual? Las clases de ELector y Candidato
# Tecnologias usadas: python flask
# Tareas Encargadas: crear la clase Elector y Candidato con python flask
# Ejemplo de clases: 
elector = Elector(id=1, correo="ejemplo@correo.com", contraseña="password123", nombre="Juan", apellido="Perez")
candidato = Candidato(id=2, correo="candidato@correo.com", contraseña="password123", nombre="Maria", apellido="Gomez",
candidatura="Presidencial", propuesta="Mejora económica")
# SOLID: Single responsability, Dependecy Inversion y principio de abierto/cerrado
# Estilos usados: Code smell, trinity y bugs
