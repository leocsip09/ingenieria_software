DOCUMENTACION DEL PROYECTO 

Principio SOLID : 
1) Single Responsibility Principle (SRP) :
   La clase AdministradorEleccion se encarga únicamente de registrar a un administrador, cumpliendo con el principio de Responsabilidad Única (SRP).

class AdministradorEleccion:
    def __init__(self):
        self.nombre = None
        self.id = None
        self.password = None

    def registrar_admin(self, nombre: str, password: str, id: int) -> None:
        self.nombre = nombre
        self.password = password
        self.id = id

2)  Open/Closed Principle (OCP):
    La clase Eleccion está diseñada para ser abierta para la extensión pero cerrada para la modificación (OCP), permitiendo añadir nuevas funcionalidades sin cambiar el código existente.

class Eleccion:
    def __init__(self, tipo_eleccion: str = None, fecha_inicio: str = None, fecha_fin: str = None):
        self.tipo_eleccion = tipo_eleccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def iniciar_eleccion(self, fecha_inicio: str) -> None:
        self.fecha_inicio = fecha_inicio

    def finalizar_eleccion(self, fecha_fin: str) -> None:
        self.fecha_fin = fecha_fin


3) Interface Segregation Principle (ISP):
   La interfaz IResultados está diseñada para proporcionar métodos específicos relacionados con la gestión de resultados, cumpliendo con el principio de Segregación de Interfaces (ISP) al asegurar que las 
   implementaciones solo dependan de métodos que realmente utilizan
from abc import ABC, abstractmethod

class IResultados(ABC):
    @abstractmethod
    def agregar_voto(self, candidato: str) -> None:
        pass

    @abstractmethod
    def calcular_porcentajes(self) -> None:
        pass

    @abstractmethod
    def mostrar_resultados(self) -> dict:
        pass
---

ESTILOS DE PROGRAMACION 
1) THINGS: El estilo "Things" se centra en representar entidades del mundo real y sus interacciones.  Estas clases encapsulan datos y comportamientos relacionados con cada entidad, facilitando la gestión y manipulación de objetos del sistema de votación
   
class AdministradorEleccion:
    def __init__(self, nombre, password, id=None):
        self.nombre = nombre
        self.password = password
        self.id = id

    def registrar_admin(self, nombre, password, id):
        self.nombre = nombre
        self.password = password
        self.id = id

    def configurar_eleccion(self, eleccion, nueva_fecha_inicio=None, nueva_fecha_fin=None, nuevos_candidatos=None):
        if nueva_fecha_inicio:
            eleccion.iniciar_eleccion(nueva_fecha_inicio)
        if nueva_fecha_fin:
            eleccion.finalizar_eleccion(nueva_fecha_fin)
        if nuevos_candidatos:
            eleccion.lista_candidatos = nuevos_candidatos

    def agregar_candidato(self, eleccion, candidato):
        eleccion.lista_candidatos.append(candidato)

    def eliminar_candidato(self, eleccion, candidato):
        if candidato in eleccion.lista_candidatos:
            eleccion.lista_candidatos.remove(candidato)

