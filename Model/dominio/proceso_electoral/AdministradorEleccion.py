#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.dominio.proceso_electoral.interfaces.Iadministrador_eleccion import IAdministradorEleccion  # Asegúrate de importar la interfaz
from Eleccion import Eleccion


class AdministradorEleccion(IAdministradorEleccion):
    def __init__(self, nombre=None, admin_id=None, password=None):
        self.nombre = nombre
        self.admin_id = admin_id
        self.password = password

    def registrar_administrador(self, nombre: str, password: str, admin_id: str) -> None:
        """Registra un administrador con el nombre, contraseña y ID proporcionados."""
        self.nombre = nombre
        self.password = password
        self.admin_id = admin_id

    def configurar_eleccion(self, eleccion: Eleccion, nueva_fecha_inicio: str = None, 
                            nueva_fecha_fin: str = None, nuevos_candidatos: list = None) -> None:
        """Configura una elección actualizando la fecha de inicio, fecha de fin y lista de candidatos."""
        if nueva_fecha_inicio:
            eleccion.iniciar_eleccion(nueva_fecha_inicio)

        if nueva_fecha_fin:
            eleccion.finalizar_eleccion(nueva_fecha_fin)

        if nuevos_candidatos is not None:
            # Modificar la lista de candidatos de la elección
            eleccion.lista_candidatos = nuevos_candidatos

    def agregar_candidato(self, eleccion: Eleccion, candidato: str) -> None:
        """Agrega un candidato a la elección."""
        eleccion.lista_candidatos.append(candidato)

    def eliminar_candidato(self, eleccion: Eleccion, candidato: str) -> None:
        """Elimina un candidato de la elección."""
        if candidato in eleccion.lista_candidatos:
            eleccion.lista_candidatos.remove(candidato)
