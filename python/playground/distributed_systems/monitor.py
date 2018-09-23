#!/usr/bin/env python

import os
import sys
import re
import yaml
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import Servidor, Grupo, Usuario, DiscoDuro


class Monitor(object):
  """docstring for Monitor"""

  # Datos de configuracion
  config = []
  # Manejador de acceso a la BD
  session = ''

  def __init__(self):
    # Enviamos mensaje de inicio
    clase = self.__class__.__name__
    print clase, "de agentes iniciado..."
    # Cargamos archivo de configuracion
    self.cargar_config()
    # Cargamos conexion a la BD
    self.conectar_db()

  def __del__(self):
    clase = self.__class__.__name__
    print clase, "de agentes destruido!"


  def inicio(self):
    """docstring for inicio"""
    # Si existen datos para el servidor actual, los borramos
    self.borrar_servidor()
    # Registramos todos los datos del servidor en la BD
    self.registrar_servidor(self.leer_group(), self.leer_passwd())
    #self.leer_capacidad()
    return 0


  def fin(self,status):
    """docstring for fin"""
    if (status == 0):
      print "Se ha ejecutado el Monitor exitosamente!"
      sys.exit(0)
    else:
      print "ERROR: Se ha generado un error durante la ejecucion del Monitor"
      sys.exit(1)


  def cargar_config(self):
    """docstring for cargar_config"""
    # Obtenemos de las variables de entorno del sistema, el directorio HOME del usuario que ejecuta el monitor
    homedir = os.environ.get("HOME")
    # Construimos el string del archivo de configuracion
    archivoConfig = homedir + '/.agente/config.yaml'
    # Abrimos el archivo en un manejador
    stream = file(archivoConfig, 'r')
    # Usando la libreria PyYaml cargamos los datos de configuracion desde el archivo
    config = yaml.load(stream)
    # Guardamos los datos en la variable global config, para que esten disponibles en todo momento
    self.config = config


  def conectar_db(self):
    """docstring for conectar_db"""
    # Construimos el string de conexion a la BD segun archivo de configuracion
    conn = ''
    conn = conn + self.config['dbengine'] + '://'
    conn = conn + self.config['dbuser'] + ':'
    conn = conn + self.config['dbpass'] + '@'
    conn = conn + self.config['dbserver'] + ':'
    conn = conn + str(self.config['dbport']) + '/'
    conn = conn + self.config['dbschema']
    # Creamos un motor de BD
    engine = create_engine(conn, echo=False)
    # Creamos un objeto de tipo Session
    Session = sessionmaker(bind=engine)
    # Obtenemos una instancia de Session que manejara todas las conexiones de la aplicacion
    self.session = Session()


  def borrar_servidor(self):
    """docstring for borrar_servidor"""
    # Guardamos un query con los datos del servidor actual
    query = self.session.query(Servidor).filter(Servidor.ser_ip==self.config['agentip'])
    # Si el servidor existe lo borramos, sino se creara desde cero
    if (query.count() == 1):
      # Obtenemos la instancia del servidor
      serv = query.one()
      # Lo agregamos al session para que sea borrado
      self.session.delete(serv)
      # Guardamos en la BD
      self.session.commit()


  def registrar_servidor(self, tuplas_grupos, tuplas_usuarios):
    """docstring for registrar_servidor"""
    # Creamos un nuevo servidor
    nuevo_s = Servidor(self.config['agentip'], self.config['agentdesc'])

    # Recorremos todos los grupos
    for tupla_g in tuplas_grupos:
      # Creamos un grupo y a continuacion le asignaremos sus correspondientes usuarios
      nuevo_g = Grupo(tupla_g[0], tupla_g[1])

      # Recorremos todos los usuarios
      for tupla_u in tuplas_usuarios:
        # Si el groupid del grupo actual es igual al groupid del usuario actual lo agregamos a su lista de usuarios
        if (nuevo_g.gru_groupid == tupla_u[1]):
          nuevo_g.usuarios.append(Usuario( tupla_u[0], tupla_u[2], tupla_u[3], tupla_u[4] ))

      # Finalmente agregamos el grupo a la lista de grupos del servidor
      nuevo_s.grupos.append( nuevo_g )
    # Guardamos en BD
    self.session.add(nuevo_s)
    self.session.commit()


  def leer_passwd(self):
    """docstring for leer_passwd"""
    # Abrimos el archivo en un manejador
    f = open('/etc/passwd','rU')
    # Leemos el archivo y lo guardamos como una sola cadena de texto
    text = f.read()
    # Cerramos el manejador
    f.close()
    # Aplicacion expresion regular para extraer la informacion necesaria
    lista_tuplas = re.findall(r'([\w-]+):x?:\d+:(\d+):(.*):([\w/-]*):([\w/-]*)', text)
    # Retorna lista de tuplas
    return lista_tuplas


  def leer_group(self):
    """docstring for leer_group"""
    # Abrimos el archivo en un manejador
    f = open('/etc/group','rU')
    # Leemos el archivo y lo guardamos como una sola cadena de texto
    text = f.read()
    # Cerramos el manejador
    f.close()
    # Aplicacion expresion regular para extraer la informacion necesaria
    lista_tuplas = re.findall(r'([\w-]+):x?:(\d+):.*', text)
    # Retorna lista de tuplas
    return lista_tuplas


def main():
  """docstring for main"""
  # Creamos una instancia del monitor
  monitor = Monitor()
  # Se inicia el monitor
  status = monitor.inicio()
  # Finaliza el monitor
  monitor.fin(status)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
