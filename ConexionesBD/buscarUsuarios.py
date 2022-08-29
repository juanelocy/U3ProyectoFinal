from ConexionesBD.ConexiónBaseDatos import *
#from ConexiónBaseDatos import *
'''
import pymongo
    La libreria pymongo es una libreria que nos permite conectarnos a una base de datos
'''
cliente=MongoDb("sistema911","localhost","27017",1000)
cliente=cliente.conectar()
baseDatos = cliente["sistema911"]
coleccion = baseDatos["usuarios"]
def retornarUsuarios():
    '''
    retornarUsuarios():
        Funcion que retorna una lista de usuarios extraido de la base de datos
    parametros:
    -----------------
        Sin parametros
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosUsuarios = []
    for i in datosDeLaColeccion:
        usuariosUsuarios.append(i['_id'])
    return usuariosUsuarios
def retornarContraseñas():
    '''
    retornarContraseñas():
        Funcion que retorna una lista de contraseñas extraido de la base de datos
    Parametros:
    -----------------
        Sin parametros
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosContraseñas = []
    for i in datosDeLaColeccion:
        usuariosContraseñas.append(i['contrasenia'])
    return usuariosContraseñas
def retornarRoles():
    '''
    retornarRoles():
        Funcion que retorna una lista de roles extraido de la base de datos
    parametros:
    -----------------
        Sin parametros
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosRoles = []
    for i in datosDeLaColeccion:
        usuariosRoles.append(i['roles'])
    return usuariosRoles