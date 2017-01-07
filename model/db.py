#!/bin/env python
#coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

session = None
modelDb = {}

def release():
    global session
    if None != session :
        session.close()

def init_engine(app):
    global session 
    engine = create_engine(app.settings["db_string"],echo = False,pool_size=20,pool_recycle=30)
    Seesion =sessionmaker(bind=engine,autoflush = True)
    session = Seesion()
    session.execute("show tables;")
    return True 

def getModel(name):
    global modelDb
    return modelDb[name]()

#wrapper one model class to modelDb
def registerModel(realModel):
    global modelDb
    name = realModel.name
    modelDb[name] = realModel

