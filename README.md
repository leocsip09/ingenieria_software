#sistema de elecciones online 
#De qué trata? Un sistema online donde realizar las votaciones, con vision de elector y candidato
#Qué encontramos en el fork actual? Las clases de ELector y Candidato
#Tecnologias usadas: python flask
#Ejemplo de clases: 
elector = Elector(id=1, correo="ejemplo@correo.com", contraseña="password123", nombre="Juan", apellido="Perez")
candidato = Candidato(id=2, correo="candidato@correo.com", contraseña="password123", nombre="Maria", apellido="Gomez", candidatura="Presidencial", propuesta="Mejora económica")
