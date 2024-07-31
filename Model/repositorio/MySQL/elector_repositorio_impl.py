#!/usr/bin/python
#-*- coding: utf-8 -*-

from Model.extensions import db
from Model.models import Elector

class elector_repositorio_impl:
    def agregar_elector(self, elector):
        try:
            db.session.add(elector)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def eliminar_elector(self, elector):
        try:
            db.session.delete(elector)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    def obtener_elector_por_correo(self, correo):
        try:
            elector = Elector.query.filter_by(correo=correo).one()
            return elector
        except NoResultFound:
            return None
