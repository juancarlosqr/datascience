#!/usr/bin/env python

import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

""" ****** New Class ****** """

class Servidor(Base):
  """docstring for Servidor"""
  __tablename__ = 'servidor'

  ser_id = Column(Integer, primary_key=True)
  ser_ip = Column(String)
  ser_nombre = Column(String)
  grupos = relationship("Grupo", back_populates="servidor", cascade="all, delete, delete-orphan")
  discos = relationship("DiscoDuro", back_populates="servidor_dis", cascade="all, delete, delete-orphan")

  def __init__(self, ser_ip, ser_nombre):
    self.ser_ip = ser_ip
    self.ser_nombre = ser_nombre
  def __repr__(self):
    return "<Servidor ('%s','%s')>" % (self.ser_ip, self.ser_nombre)

""" ****** New Class ****** """

class Grupo(Base):
  """docstring for Servidor"""
  __tablename__ = 'grupo'

  gru_id = Column(Integer, primary_key=True)
  gru_grupo = Column(String)
  gru_groupid = Column(Integer)
  servidor_ser_id = Column(Integer, ForeignKey('servidor.ser_id'))
  servidor = relationship("Servidor", back_populates="grupos")
  usuarios = relationship("Usuario", back_populates="grupo", cascade="all, delete, delete-orphan")

  def __init__(self, gru_grupo, gru_groupid):
    self.gru_grupo = gru_grupo
    self.gru_groupid = gru_groupid
  def __repr__(self):
    return "<Grupo ('%s','%s')>" % (self.gru_grupo, self.gru_groupid)

""" ****** New Class ****** """

class Usuario(Base):
  """docstring for Usuario"""
  __tablename__ = 'usuario'

  usu_id = Column(Integer, primary_key=True)
  usu_usuario = Column(String)
  usu_descripcion = Column(String)
  usu_directorio = Column(String)
  usu_shell = Column(String)
  grupo_gru_id = Column(Integer, ForeignKey('grupo.gru_id'))
  grupo = relationship("Grupo", back_populates="usuarios")

  def __init__(self, usu_usuario, usu_descripcion, usu_directorio, usu_shell):
    self.usu_usuario = usu_usuario
    self.usu_descripcion = usu_descripcion
    self.usu_directorio = usu_directorio
    self.usu_shell = usu_shell
  def __repr__(self):
    return "<Usuario ('%s','%s','%s','%s')>" % (self.usu_usuario, self.usu_descripcion, self.usu_directorio, usu_shell)

""" ****** New Class ****** """

class DiscoDuro(Base):
  """docstring for DiscoDuro"""
  __tablename__ = 'disco_duro'

  dis_id = Column(Integer, primary_key=True)
  dis_nombre = Column(String)
  dis_tamano = Column(String)
  dis_usado = Column(String)
  dis_disponible = Column(String)
  dis_usado_porcen = Column(String)
  dis_montado = Column(String)
  servidor_ser_id = Column(Integer, ForeignKey('servidor.ser_id'))
  servidor_dis = relationship("Servidor", back_populates="discos")

  def __init__(self, dis_nombre, dis_tamano, dis_usado, dis_disponible, dis_usado_porcen, dis_montado ):
    self.dis_nombre = dis_nombre
    self.dis_tamano = dis_tamano
    self.dis_usado = dis_usado
    self.dis_disponible = dis_disponible
    self.dis_usado_porcen = dis_usado_porcen
    self.dis_montado = dis_montado
  def __repr__(self):
    return "<DiscoDuro ('%s','%s','%s','%s')>" % (self.dis_nombre, self.dis_tamano, self.dis_usado, self.dis_disponible)
