#!/usr/bin/python
#-*- coding: utf-8 -*-
from Model.extensions import db
from Model.models.registro_electoral import RegistroElectoralModelo

class registro_electoral_repositorio_impl:
    @staticmethod
    def ingresar_nuevo_registro(registro):
        try:
            db.session.add(registro)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @staticmethod
    def eliminar_registro(registro):
        try:
            entrada = db.session.query(RegistroElectoralModelo).filter_by(id = registro.id).one()
            db.session.delete(entrada)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()