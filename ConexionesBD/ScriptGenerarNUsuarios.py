import pandas as pd
import random as r
import time
from ConexiónBaseDatos import*
from buscarUsuarios import *
data = pd.read_csv("ConexionesBD\BaseUsuarios.csv")
'''
data=pd.read_csv("ScriptUsuarios\BaseUsuarios.csv"):
    Sintaaxís para abrir el archivo csv y obtener los datos separados en un diccionario
'''
def obtenerDatosPorSeparados():
    '''
    def obtenerDatosPorSeparados():
        Funcion que obtiene los datos separados en diferentes  diccionarios
    '''
    nombres=[]
    apellidos=[]
    telefonos=[]
    direcciones=[]
    nombres = data["nombre"]
    apellidos = data["apellido"]
    telefonos= data["telefono"]
    direcciones = data["direccion"]
    return nombres, apellidos, telefonos, direcciones
def generarUsuarios(cantidadUsuarios):
    '''
    generarUsuarios(cantidadUsuarios):
        Funcion que genera N cantidad de usuarios en una coleccion, y luego es insertada en mongo db
    Parametros:
    -----------------
        Sin parametros
    Atributos:
    -----------------
        nombres: 
            Tipo lista, que contiene los nombres de los usuarios a generar
        apellidos: 
            Tipo lista, que contiene los apellidos de los usuarios a generar
        telefonos: 
            Tipo lista, que contiene los telefonos de los usuarios a generar
        direcciones: 
            Tipo lista, que contiene las direcciones de los usuarios a generar
        cliente:  
            Tipo pymongo.MongoClient, que contiene el cliente de la base de datos a conectar
        coleccion: 
            Tipo String, que contiene el nombre de la coleccion a generar
        cedula: 
            Tipo String, que contiene la cedula del usuario a guardar en la base de datos
        documento: 
            Tipo diccionario, que contiene los datos del usuario a guardar en la base de datos
    '''
    conectarMongo=MongoDb("sistema911","localhost","27017",1000)
    nombres=obtenerDatosPorSeparados()[0]
    apellidos=obtenerDatosPorSeparados()[1]
    telefonos=obtenerDatosPorSeparados()[2]
    direcciones=obtenerDatosPorSeparados()[3]
    diccionarios=[]
    listaIdRoles=conectarMongo.retornarIds(conectarMongo.conectar(),"roles")
    for i in range(cantidadUsuarios):
        idRandom=listaIdRoles[r.randint(0,len(listaIdRoles)-1)]
        nuevoRol=conectarMongo.buscarId(conectarMongo.conectar(), "roles", int(idRandom))
        cedula=r.randint(2000000000,9999999999)
        diccionarios.append({"_id":cedula,"nombre":nombres[r.randint(0,999)],"apellido":apellidos[r.randint(0,999)],"telefono":telefonos[r.randint(0,999)],"direccion":direcciones[r.randint(0,999)], "avenida":direcciones[r.randint(0,999)],"callePrincipal":direcciones[r.randint(0,999)],"calleSecundaria":direcciones[r.randint(0,999)], "caso": "", "observaciones":"", "usuario":"", "contrasenia":"", "roles":nuevoRol})
    datosGuardados=conectarMongo.guardarUsuario(conectarMongo.conectar(),"usuarios", diccionarios)
    if datosGuardados==True:
        print("Usuarios registrados correctamente")
    else:
        print("Error al registrar usuarios")




    