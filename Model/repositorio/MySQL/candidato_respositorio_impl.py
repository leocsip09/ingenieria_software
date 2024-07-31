#!/usr/bin/python
#-*- coding: utf-8 -*-
from Model.extensions import db
from Model.models import Candidato

class candidato_respositorio_impl:
    def agregar_candidato(self, candidato):
        try:
            db.session.add(candidato)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def eliminar_candidato(self, candidato):
        try:
            db.session.delete(candidato)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def obtener_candidato_por_id(self, id):
        try:
            candidato = Candidato.query.get(id)
            return candidato
        except Exception as e:
            return None