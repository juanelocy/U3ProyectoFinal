from ConexiónBaseDatos import*
def menuPrincipal():
    '''
    def menuPrincipal():
        Procedimiento que me permite ejecutar el programa principal.
    '''
    print("-----------------------------------------------------")
    print("                 MENÚ PRINCIPAL")
    print("-----------------------------------------------------")
    print("1..............................Para guardar 1 usuario")
    print("2..............................Para agregar Rol")
    print("3..............................Para agregar Permiso")
    opcion=int(input("Ingrese una opción: "))
    if opcion==1:
        agregarUsuarioNuevo()
    elif opcion==2:
        agregarNuevoRol()
    elif opcion==3:
        agregarPermisos()
    else:
        print("-----------------------------------------------------")
        print("|              No existe esta opción                  |")
        print("|     Lo redireccionaremos al menú [Principal]        |")
        print("-----------------------------------------------------")
        print ("                       |")
        print ("                       |")
        print ("                       |")
        print ("                       |")
        print ("                       V")
        print(opcion)
        menuPrincipal()
def agregarUsuarioNuevo():
    '''
    def agregarUsuarioNuevo():
        Procedimiento que me permite agregar un nuevo usuario a la colección usuarios.
    parametros del procedimiento:
    -------------
        ninguno
    Parámetros
    -------------
        nombreUsuario: str
            Nombre del usuario que se va a agregar
        contraseña: str
            Contraseña del usuario que se va a agregar
        rol: str
            Rol del usuario que se va a agregar
    '''
    conectarMongo=MongoDb("sistema911", "localhost", "27017", 1000)
    try:            
        idRol=int(input("Ingrese el id del rol : "))
        idEncontrada=conectarMongo.buscarId(conectarMongo.conectar(), "roles", idRol)
        if idEncontrada==[]:
            print("--------------------------------------------")
            print("      NO SE ENCONTRÓ EL ID DEL ROL")
            print("--------------------------------------------")
        else:
            nuevoUsuario={"nombre":"LuisEjempl", "apellido":"GuachilemaEjemplo", "rol":idEncontrada}
            conectarMongo.guardarUsuario2(conectarMongo.conectar(),"usuarios2", nuevoUsuario)
            print("Se ha creado correctamente el usuario")
    except:
        print("Lo sentimos sucedio un error inesperado")
def agregarNuevoRol():
    '''
    def agregarNuevoRol():
        Procedimiento que me permite agregar un nuevo rol a la colección roles.
    Parámetros del procedimiento:
    -------------
        ninguno
    Parámetros 
    -------------
        nombreRol: str
            Nombre del rol que se va a agregar
        descripcion: str
            Descripción del rol que se va a agregar
        cantidadPermisos: int
            Cantidad de permisos que se van a asignar al rol
    '''
    conectarMongo=MongoDb("sistema911", "localhost", "27017", 1000)
    nombreRol=str(input("Ingrese el nombre del rol: "))
    idRol=int(input("Ingrese el id del rol:"))
    cantidadPermisos=int(input("Ingrese el número de permisos que va a tener el rol: ")) 
    if asignarNPermisosAunRol(cantidadPermisos)==True:
        listaPermisos=[]
        for i in range(cantidadPermisos):
            print("-------------------------------------------")
            print("             Permiso #",int(i+1))
            print("-------------------------------------------")
            idPermiso=int(input("Ingrese el id del permiso: "))      
            permiso=conectarMongo.buscarId(conectarMongo.conectar(), "permisos", idPermiso)
            if permiso==[]:
                print("--------------------------------------------")
                print("      NO SE ENCONTRÓ EL ID DEL PERMISO")
                print("--------------------------------------------")
            else:
                permiso=permiso[0]
                listaPermisos.append(permiso)
        try:
            rolNuevo={"_id":idRol, "rol":nombreRol, "permisos":listaPermisos}
            conectarMongo.guardarUsuario2(conectarMongo.conectar(), "roles", rolNuevo)
            print("Se ha creado correctamente el rol")
        except:
            print("Lo sentimos sucedio un error inesperado")
    else:
        print("-----------------------------------------------------")
        print("   Lo sentimos los permisos están fuera del rango")
        print("  de los permisos disponibles en la base de datos ")
        print("-----------------------------------------------------")
def agregarPermisos():
    '''
    def agregarPermisos():
        Procedimiento que me permite agregar un nuevo permiso a la colección permisos.
    Parámetros del procedimiento:
    -------------
        ninguno
    Parámetros
    -------------
        numerosPermisos: int
            Número de permisos que se van a agregar
    '''
    print("--------------------------------------------------------")    
    print("                 AGREGAR PERMISMOS")
    print("--------------------------------------------------------")    
    numeroPermisos=int(input("Ingrese el número de permisos: "))
    listapermisos=[]
    for i in range(numeroPermisos):
        print("-------------------------------------------")
        print("             Permiso #",int(i+1))
        print("-------------------------------------------")
        idPermiso=int(input("Ingrese el id del permiso: "))
        nombrePermiso=str(input("Ingrese el nombre del permiso: "))
        descripcion=str(input("Ingrese la descripción del permiso: "))        
        permisoNuevo={"_id":idPermiso, "permiso":nombrePermiso, "descripcion":descripcion}
        listapermisos.append(permisoNuevo)
    try:
        conectarMongo=MongoDb("sistema911", "localhost", "27017", 1000)
        conectarMongo.guardarUsuario(conectarMongo.conectar(),"permisos",listapermisos)
    except:
        print("Lo sentimos sucedio un error inesperado")
def asignarNPermisosAunRol(cantindadPermisos):
    '''
    def asignarNPermisosAunRol(cantindadPermisos):
        Función que me permite asignar N permisos a un rol, retorna true si el número de permisos ingresado
        está dentro del rango de permisos existente en la colección permisos.
    Parametros:
    -------------
        cantindadPermisos: int
            Cantidad de permisos que se van a asignar al rol
    '''
    conectarMongo=MongoDb("sistema911", "localhost", "27017", 1000)
    numeroPermisos=conectarMongo.cantidadRegistros(conectarMongo.conectar(), "permisos")
    if cantindadPermisos>numeroPermisos or cantindadPermisos<0:
        return False
    else:
        return True 
if __name__=="__main__":
    menuPrincipal()
