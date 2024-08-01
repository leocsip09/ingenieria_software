#!/usr/bin/python
# -*- coding: utf-8 -*-

from Model.dominio.proceso_electoral.interfaces.Iregistro_electoral_repositorio import IRegistroElectoralRepositorio


class RegistroElectoral(IRegistroElectoralRepositorio):
    def __init__(self):
        """Inicializa las listas de electores, candidatos y partidos."""
        self.lista_electores = []  
        self.lista_candidatos = []  
        self.lista_partidos = []  
        
    def agregar_elector(self, elector) -> None:
        """Agrega un elector a la lista de electores."""
        self.lista_electores.append(elector)

    def eliminar_elector(self, elector) -> None:
        """Elimina un elector de la lista de electores."""
        if elector in self.lista_electores:
            self.lista_electores.remove(elector)

    def agregar_candidato(self, candidato) -> None:
        """Agrega un candidato a la lista de candidatos."""
        self.lista_candidatos.append(candidato)

    def eliminar_candidato(self, candidato) -> None:
        """Elimina un candidato de la lista de candidatos."""
        if candidato in self.lista_candidatos:
            self.lista_candidatos.remove(candidato)

    def agregar_partido(self, partido) -> None:
        """Agrega un partido a la lista de partidos."""
        self.lista_partidos.append(partido)

    def eliminar_partido(self, partido) -> None:
        """Elimina un partido de la lista de partidos."""
        if partido in self.lista_partidos:
            self.lista_partidos.remove(partido)
