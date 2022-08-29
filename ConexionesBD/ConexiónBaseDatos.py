from abc import ABC, abstractmethod
import pymongo
class conectarseBaseDeDatos(ABC):
    '''
    class conectarseBaseDeDatos(ABC):
        Clase abstracta para conectar a la base de datos MongoDb
    Atributos: 
    -----------------
        nombreBaseDatos: Tipo String, que contiene el nombre de la base de datos a conectar
    Métodos abstractos:
    -------------------
    def conectar(self,host,port,tiempofuera):
        Método abstracto para conectar a la base de datos MongoDb mediante el host, puerto y tiempo de espera 
    '''
    @abstractmethod
    def __init__(self, nombreBaseDeDatos, host, puerto, tiempoFuera):
        '''
        def __init__(self, nombreBaseDeDatos):
            Metodo constructor de la clase conectarseBaseDeDatos, el cual es un método abstracto y necesita el nombre de la base de 
            con la que se quiere conectar a MongoDb
        Atributos:
        -----------------
            nombreBaseDeDatos: Tipo String, que contiene el nombre de la base de datos a conectar
        '''
        nombreBaseDeDatos=nombreBaseDeDatos
        self.host=host
        self.puerto=puerto
        self.tiempoFuera=tiempoFuera
    @abstractmethod
    def conectar(self):
        '''
        def conectar(self, host, puerto, tiempoFuera):
            Método abstracto para conectar a la base de datos MongoDb mediante el host, puerto y tiempo de espera
            el cual está vacía porque al conectar a cualquier otra base de datos se debe implementar el método 
            ya que que un diferente en cada base de datos, pero si o si existe un método para conectar a la base de datos
            y dependiendo la base dato se reecribirá el método conectar en cada clase hija.
        Parametros:
        -----------------
            host: Tipo String, que contiene el host de la base de datos a conectar
            puerto: Tipo Int, que contiene el puerto de la base de datos a conectar
            tiempoFuera: Tipo Int, que contiene el tiempo de espera de la base de datos a conectar
        '''
        pass
class MongoDb(conectarseBaseDeDatos):
    '''
    Class mongoDb(conectarseBaseDeDatos): 
        Clase que hereda de la clase conectarseBaseDeDatos y contiene el método conectar para conectar a la base de datos MongoDb
    Atributos:
    -----------------
        nombreBaseDeDatos: Tipo String, que contiene el nombre de la base de datos a conectar (MONGO)
    Métodos:
    -------------------
        def __init__(self, nombreBaseDeDatos):
            Metodo constructor de la clase mongoDb, el cual es un método abstracto y necesita el nombre de la base de datos a conectar
        def conectar(self, host, puerto, tiempoFuera):
            Método para conectar a la base de datos MongoDb mediante el host, puerto y tiempo de espera
        def eliminarColeccion(self, cleinte, nombreColeccion):
            Método para eliminar la coleccion de la base de datos MongoDb
    '''
    def __init__(self, nombreBaseDeDatos,host, puerto, tiempoFuera):
        '''
        def __init__(self, nombreBaseDeDatos):
            Metodo constructor de la clase MongoDb, el cual es un método abstracto y necesita el nombre de la base de datos a conectar
        Atributos:
        -----------------
            nombreBaseDeDatos: Tipo String, que contiene el nombre de la base de datos a conectar (MONGO)        
        '''
        self.nombreBaseDeDatos=nombreBaseDeDatos
        self.host=host
        self.puerto=puerto
        self.tiempoFuera=tiempoFuera
    def conectar(self):
        '''
        def conectar(self, host, puerto, tiempoFuera):
            Método para conectar a la base de datos MongoDb mediante el host, puerto y tiempo de espera
        Parametros:
        -----------------
            host: Tipo String, que contiene el host de la base de datos a conectar
            puerto: Tipo Int, que contiene el puerto de la base de datos a conectar
            tiempoFuera: Tipo Int, que contiene el tiempo de espera de la base de datos a conectar
        '''
        NOMBRECOLECCION="sistemaDeEmergencia911"
        MONGO_URI = "mongodb://"+self.host+":"+self.puerto+"/"
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=self.tiempoFuera)
        return cliente
    def eliminarColeccion(self, cleinte, nombreColeccion):
        '''
        def eliminarColeccion(self, cleinte, nombreColeccion):
            Método para eliminar la coleccion de la base de datos MongoDb
        Parametros:
        -----------------
            cleinte: Tipo pymongo.MongoClient, que contiene el cliente de la base de datos a conectar
            nombreColeccion: Tipo String, que contiene el nombre de la coleccion a eliminar
        '''
        try:
            miBaseDatos=cleinte[self.nombreBaseDeDatos]
            miColeccion=miBaseDatos[nombreColeccion]
            miColeccion.drop()
            print("La coleccion Eliminada es: "+nombreColeccion)
        except:
            print("Error al eliminar la coleccion")
    def mostrarColecciones(self, cleinte):
        '''
        def mostrarColecciones(self, cleinte):
            Método para mostrar las colecciones de la base de datos MongoDb y ne retorna una lista con las colecciones de la base de datos ingresada 
        Parametros:
        -----------------
            cleinte: Tipo pymongo.MongoClient, que contiene el cliente de la base de datos a conectar
        '''
        miBaseDatos=cleinte[self.nombreBaseDeDatos]
        return miBaseDatos.list_collection_names()
    def buscarId(self, cliente, coleccion,id):
        miBaseDatos=cliente[self.nombreBaseDeDatos]                            
        micoleccion=miBaseDatos[coleccion]
        '''
        buscarId(id):
            Funcion que retorna una lista de usuarios extraido de la base de datos
        Parametros:
        -----------------
            cliente:
                Parametro que contiene el cliente de la base de datos a conectar
            coleccion:  
                Parametro que contiene la coleccion de la base de datos a conectar
            id:
                Parametro que contiene el id a buscar
        '''
        datosDeLaColeccion = micoleccion.find()
        usuariosUsuarios = []
        for i in datosDeLaColeccion:
            if i['_id'] == id:
                usuariosUsuarios.append(i)
        return usuariosUsuarios

    def guardarUsuario(self, cliente, coleccion, documento):
        '''
        def guardarUsuario(documento):
            Funcion pra guardar un documento en la coleccion en MongoDb y retorna un true o false
            True si se guardo correctamente, False si no se guardo, validando con try except
        Parametro:
        -----------------
            documento: Tipo diccionario, que contiene los datos del usuario a guardar en la base de datos
        '''
        miBaseDatos=cliente[self.nombreBaseDeDatos]
        micoleccion=miBaseDatos[coleccion]
        try:
            micoleccion.insert_many(documento)
            return True
        except:
            return False
    def guardarUsuario2(self, cliente, coleccion, documento):
        miBaseDatos=cliente[self.nombreBaseDeDatos]
        micoleccion=miBaseDatos[coleccion]
        '''
        def guardarUsuario(documento):
            Funcion pra guardar un documento en la coleccion en MongoDb y retorna un true o false
            True si se guardo correctamente, False si no se guardo, validando con try except
        Parametro:
        -----------------
            documento: Tipo diccionario, que contiene los datos del usuario a guardar en la base de datos
        '''
        try:
            micoleccion.insert_one(documento)
            return True
        except:
            return False
    def actualizarUsuario(self, cliente, coleccion, documento, cedula):
        miBaseDatos=cliente[self.nombreBaseDeDatos]
        micoleccion=miBaseDatos[coleccion]
        '''
        def actualizarUsuario(documento):
            Funcion pra actualizar un documento en la coleccion en MongoDb y retorna un true o false
            True si se actualizo correctamente, False si no se actualizo, validando con try except
        Parametro:
        -----------------
            documento: Tipo diccionario, que contiene los datos del usuario a actualizar en la base de datos
        '''
        try:
            micoleccion.update_one({'_id':cedula}, {"$set": documento})
            return True
        except:
            return False  
    def cantidadRegistros(self, cliente, coleccion):
        '''
        def cantidadRegistros():
            Método para contar la cantidad de registros de la base de datos
        Parametros:
        -----------------
            cleinte: Tipo pymongo.MongoClient, que contiene el cliente de la base de datos a conectar
            nombreColeccion: Tipo String, que contiene el nombre de la coleccion a contar
        '''
        miBaseDatos=cliente[self.nombreBaseDeDatos]
        micoleccion=miBaseDatos[coleccion]
        documentos=micoleccion.count_documents({})
        return documentos
    def retornarIds(self, cliente, coleccion):
        '''
        retornarUsuarios():
        Funcion que retorna una lista de usuarios extraido de la base de datos
        '''
        miBaseDatos=cliente[self.nombreBaseDeDatos]
        micoleccion=miBaseDatos[coleccion]
        datosDeLaColeccion = micoleccion.find()
        usuariosUsuarios = []
        for i in datosDeLaColeccion:
            usuariosUsuarios.append(i['_id'])
        return usuariosUsuarios
    def actualizarUsuario2(self, cliente, coleccion, cedula, casoAntiguo, caso, observacionAntigua,observacion):
        miBaseDatos=cliente[self.nombreBaseDeDatos]
        micoleccion=miBaseDatos[coleccion]
        '''
        def actualizarUsuario(documento):
            Funcion pra actualizar un documento en la coleccion en MongoDb y retorna un true o false
            True si se actualizo correctamente, False si no se actualizo, validando con try except
        Parametro:
        -----------------
            documento: Tipo diccionario, que contiene los datos del usuario a actualizar en la base de datos
        '''
        nuevoCaso=casoAntiguo+", "+ caso
        nuevaObservacion=observacionAntigua+", "+ observacion
        try:
            micoleccion.update_one({'_id':cedula}, {"$set": {"caso":nuevoCaso}})
            micoleccion.update_one({'_id':cedula}, {"$set": {"observaciones":nuevaObservacion}})
            return True
        except:
            return False  
if __name__=="__main__":
    pass
    




    
    