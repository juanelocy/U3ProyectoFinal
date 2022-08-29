from ScriptGenerarNUsuarios import*
def menuPrincipal():
    '''
    def menuPrincipal():
        Procedimiento que muestra el menu principal del programa, valiando con el try except los posibles errores que puedan ocurrir.
    '''
    try:
        print("-----------------------------------------------------")
        print("               MENÚ PRINCIPAL")
        print("-----------------------------------------------------")
        print("Ingrese 1..........: Para insertar N usuarios")
        print("Ingrese 2..........: Para Eliminar Colecciones")
        print("Ingrese 3..........: Para mostrar Colecciones")
        print("Ingrese 4..........: Para Salir")
        opcion=int(input("Ingrese una opción: "))
        if opcion==1:
            print("--------------------------------------------")
            print("          REGISTRAR N USUARIOS")
            print("--------------------------------------------")
            cantidadUsuarios=int(input("Cuántos Usuarios desea registrar: "))
            generarUsuarios(cantidadUsuarios)
        elif opcion==2:
            ConectarMongoDb=MongoDb("sistema911","localhost","27017",1000)
            print("-------------------------------------------")
            print("          ELIMINAR COLECCION")
            print("-------------------------------------------")
            ConectarMongoDb.eliminarColeccion(ConectarMongoDb.conectar(),"usuarios")
        elif opcion==3:
            print("-------------------------------------------")
            print("          MOSTRAR COLECCIONES")
            print("-------------------------------------------")
            ConectarMongoDb=MongoDb("sistema911", "localhost", "27017", 1000)
            print(ConectarMongoDb.mostrarColecciones(ConectarMongoDb.conectar()))
        elif opcion==4:
            print("-----------------------------------------------------")
            print("       Gracias por usar nuestro sistema")
            print("-----------------------------------------------------")
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
            menuPrincipal()
    except:
        print("-----------------------------------------------------")
        print("|       No puede ingresar valores no numéricos        |")
        print("|      Lo redireccionaremos al menú [Principal]       |")
        print("-----------------------------------------------------")
        print ("                       |")
        print ("                       |")
        print ("                       |")
        print ("                       |")
        print ("                       V")
        menuPrincipal()