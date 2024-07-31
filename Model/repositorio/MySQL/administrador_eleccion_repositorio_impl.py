#!/usr/bin/python
#-*- coding: utf-8 -*-
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from Model.extensions import db
from Model.models.administrador_eleccion import Administrador

class AdministradorEleccionRepositorioImpl:
    @staticmethod
    def insertar_administrador(admin):
        with db.session as session:
            session = sessionmaker(bind=Engine)
            try:
                session.add(admin)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
    
    @staticmethod
    def eliminar_administrador(admin):
        with db.session as session:
            session = sessionmaker(bind=Engine)
            try:
                entrada = session.query(Administrador).filter_by(id = admin.id).one()
                session.delete(entrada)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()