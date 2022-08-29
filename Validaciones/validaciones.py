import datetime
import re
def fechaRegistro():
    '''
    Funcion que devuelve la fecha actual en formato dd/mm/aaaa
    '''
    fechaActual= datetime.datetime.now().strftime("%d/%m/%Y")
    return fechaActual
fechaActual= fechaRegistro()
def horaRegistro():
    '''
    Funcion que devuelve la hora actual en formato hh:mm:ss
    '''
    horaActual= datetime.datetime.now().strftime("%H:%M:%S")
    return horaActual
horaActual= horaRegistro()
def validarContraseña(contraseñaValidar):
    '''
    Funcion que valida que la contraseña sea segura con minimo 11 digitos
    '''
    if (re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$", contraseñaValidar)and len(contraseñaValidar)>=11 and len(contraseñaValidar)<=20):
        return True
    else:
        return False
def validarCaracteres(cadenaValidar):
    '''
    Funcion que valida que la cadena solo contenga letras
    '''
    if re.match("^[a-zA-Z]*$", cadenaValidar)and len(cadenaValidar)>0 and len(cadenaValidar)<=25:
        return True
    else:
        return False
def validarNumero(numeroValidar):
    '''
    Funcion que valida que la cadena solo contenga numeros
    '''
    if re.match("^[0-9]*$", numeroValidar ) and len(numeroValidar)==10:
        numeroValidar=int(numeroValidar)
        if numeroValidar>0 :
            return True
        else:
            return False
    else:
        return False
def validarEmail(emailValidar):
    '''
    Funcion que valida que el correo solo sea (@gmail.com) o (@espe.edu.ec)
    '''
    if re.match("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$", emailValidar):
        if re.match("^[a-zA-Z0-9.+_-]+@[gmail]+\.[com]+$", emailValidar):
            return True
        else:
            if re.match("^[a-zA-Z0-9.+_-]+@[espe.edu]+\.[ec]+$", emailValidar):
                return True
            else:
                return False
    else:
        return False
def validarFecha(fechaValidar):
    '''
    Funcion que valida que la fecha sea correcta
    '''
    if re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$", fechaValidar):
        print("Fecha correcta")
        return True
    else:
        print("Fecha incorrecta")
        return False
def validarDatoVacio(datoValidar):
    '''
    Funcion que valida que el dato no este vacio
    '''
    if datoValidar=="":
        return False
    else:
        return True