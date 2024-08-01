# DOCUMENTACION DEL PROYECTO 

## Principio SOLID : 
1. Single Responsibility Principle (SRP) :
   La clase AdministradorEleccion se encarga únicamente de registrar a un administrador, cumpliendo con el principio de Responsabilidad Única (SRP).

```python
class AdministradorEleccion:
    def __init__(self):
        self.nombre = None
        self.id = None
        self.password = None

    def registrar_admin(self, nombre: str, password: str, id: int) -> None:
        self.nombre = nombre
        self.password = password
        self.id = id
```

2.  Open/Closed Principle (OCP):
    La clase Eleccion está diseñada para ser abierta para la extensión pero cerrada para la modificación (OCP), permitiendo añadir nuevas funcionalidades sin cambiar el código existente.

```python
class Eleccion:
    def __init__(self, tipo_eleccion: str = None, fecha_inicio: str = None, fecha_fin: str = None):
        self.tipo_eleccion = tipo_eleccion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def iniciar_eleccion(self, fecha_inicio: str) -> None:
        self.fecha_inicio = fecha_inicio

    def finalizar_eleccion(self, fecha_fin: str) -> None:
        self.fecha_fin = fecha_fin
```

3. Interface Segregation Principle (ISP):
   La interfaz IResultados está diseñada para proporcionar métodos específicos relacionados con la gestión de resultados, cumpliendo con el principio de Segregación de Interfaces (ISP) al asegurar que las 
   implementaciones solo dependan de métodos que realmente utilizan
from abc import ABC, abstractmethod

```python
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
```

## ESTILOS DE PROGRAMACION 
1. THINGS: El estilo "Things" se centra en representar entidades del mundo real y sus interacciones.  Estas clases encapsulan datos y comportamientos relacionados con cada entidad, facilitando la gestión y manipulación de objetos del sistema de votación

```python
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
```

3.  Error/Exception Handling: Este enfoque mejora el manejo de errores utilizando excepciones. Al usar raise ValueError para señalar problemas específicos, el código se vuelve más robusto y es más fácil de depurar, ya que los errores se identifican y manejan claramente.

```python
class Voto:
    def __init__(self):
        """Inicializa un nuevo objeto Voto con valores predeterminados."""
        self.fecha: Optional[datetime] = None
        self.hora: Optional[datetime] = None
        self.elector: Optional[str] = None  # Suponiendo que elector es un string con el nombre
        self.id_voto: Optional[str] = None  # Suponiendo que id_voto es un string

    def registrar_voto(self, elector: str, id_voto: str, fecha: Optional[datetime] = None, hora: Optional[datetime] = None) -> None:
        """Registra un voto con el elector y el ID, y establece la fecha y la hora actuales si no se proporcionan."""
        self.elector = elector
        self.id_voto = id_voto
        
        if fecha is None:
            self.fecha = datetime.now().date()
        else:
            self.fecha = fecha

        if hora is None:
            self.hora = datetime.now().time()
        else:
            self.hora = hora

    def confirmar_voto(self):
        if not self.elector:
            raise ValueError("Elector no proporcionado.")
        if not self.fecha:
            raise ValueError("Fecha no proporcionada.")
        if not self.hora:
            raise ValueError("Hora no proporcionada.")
        if not self.id_voto:
            raise ValueError("ID de voto no proporcionado.")
        print("Voto confirmado")
        return True
```

3. PIPELINE : procesar datos a través de una serie de pasos, donde la salida de un paso se convierte en la entrada del siguiente
class Resultados(IResultados):

```python
   def __init__(self):
        """Inicializa la clase Resultados con total de votos y listas vacías."""
        self.total_votos: int = 0
        self.votos_candidatos: List[int] = []  # Lista de votos por candidato
        self.porcentajes_candidatos: List[float] = []  # Lista de porcentajes por candidato

    def agregar_votos(self, votos_candidatos: List[int]) -> None:
        """Añade los votos de los candidatos y actualiza el total de votos."""
        if not all(isinstance(voto, int) for voto in votos_candidatos):
            raise ValueError("Todos los votos deben ser enteros.")
        
        self.votos_candidatos = votos_candidatos
        self.total_votos = sum(votos_candidatos)
        self.calcular_porcentajes()

    def calcular_porcentajes(self) -> None:
        """Calcula el porcentaje de votos que obtuvo cada candidato."""
        if self.total_votos > 0:
            self.porcentajes_candidatos = [(votos / self.total_votos) * 100 for votos in self.votos_candidatos]
        else:
            self.porcentajes_candidatos = [0 for _ in self.votos_candidatos]

    def get_votos_totales(self) -> int:
        """Retorna el total de votos."""
        return self.total_votos

    def get_votos_candidatos(self) -> List[int]:
        """Retorna la lista de votos por candidato."""
        return self.votos_candidatos

    def get_porcentajes_candidatos(self) -> List[float]:
        """Retorna la lista de porcentajes de votos por candidato."""
        return self.porcentajes_candidatos

    def publicar_resultados(self) -> dict:
        """Publica los resultados mostrando los votos totales y los porcentajes por candidato."""
        return {
            "total_votos": self.get_votos_totales(),
            "votos_candidatos": self.get_votos_candidatos(),
            "porcentajes_candidatos": self.get_porcentajes_candidatos()
        }
```
