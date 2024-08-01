from Model.dominio.proceso_electoral.interfaces import Iadministrador_eleccion, Ieleccion, Iregistro_electoral_repositorio, Iresultados
from participantes import Elector
from proceso_electoral import AdministradorEleccion,Eleccion,RegistroElectoral,Resultados

__all__ = [
    "Elector",
    "AdministradorEleccion",
    "RegistroElectoral",
    "Resultados",
    "Iadministrador_eleccion",
    "Ieleccion",
    "Iregistro_electoral_repositorio",
    "Iresultados"
]