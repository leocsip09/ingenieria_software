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

   
