
'''Libreria para realizar pdfs dentro de python'''
from fpdf import FPDF

def pdf(cedula, nombres, apellidos, celular, callePrincipal, calleSecundaria, descripcion):
        '''ingreso de datos '''
        '''
        P = hoja en vertical
        L = hoja en Horizontal
        A4=210x297mm
        '''

        '''Creacion del formato de un pdf o del documento'''
        pdf = FPDF(orientation='P', unit='mm', format='A4')

        '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
        '''CARATULA'''
        '''Metodo add_page para agregar una pagina'''
        pdf.add_page()
        '''Agregar imagenes, o logos'''
        pdf.image('../../Desktop/ProyectoPoo/logo.png',
                x=45 , y= 60,
                w=120 , h=100)

        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times','B',15)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        pdf.text(x=55, y=40, txt='DEPARTAMENTO OFICIAL DE REPORTES')

        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times','B',13)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        pdf.text(x=35, y=50, txt='"REPORTES POLICIALES DE SANTO DOMINGO DE LOS TSACHILAS"')

        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times','B',13)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        pdf.text(x=95, y=160, txt='LEYENDA')
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times','I',13)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        pdf.text(x=12, y=170, txt='El Servicio Integrado de Seguridad GUAYASIG 911 (SIS GUAYASIG 911) creado mediante Decreto')
        pdf.text(x=27, y=175, txt='Ejecutivo 988 del 29 de diciembre de 2011 cuenta con una plataforma tecnológica y')
        pdf.text(x=34, y=180, txt='protocolos de gestión operativa, para la recepción de llamadas y atención de')
        pdf.text(x=30, y=185, txt='emergencias, colabora con el sistema de justicia del país, como es en el uso de las')
        pdf.text(x=30, y=190, txt='instalaciones, conectividad y acceso de personal técnico del Ministerio de Justicia')
        pdf.text(x=28, y=195, txt='Derechos Humanos y Cultos (MJDHC) para el monitoreo del Sistema de Vigilancia')
        pdf.text(x=95, y=200, txt='Electrónica.')

        '''Planta baja de la caratula'''
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times','B',15)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        pdf.text(x=45, y=230, txt='SANTO DOMINGO DE LOS TSACHILAS - ECUADOR')
        pdf.text(x=95, y=240, txt='2011 - 2022')
        '''fin de hoja'''
        '''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

        '''Nueva hoja'''
        '''Agregar una nueva hoja con la funcion .add_page'''
        pdf.add_page()
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times', 'B', 30)
        pdf.text(x=80, y=30, txt='REPORTE')

        '''primer tanda'''
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times', 'B', 12)
        '''funcion ln() para dejar el espaciado de cada celda'''
        pdf.ln(40)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        pdf.cell(w=30, h=15, txt='ID', border=1, align='C', fill=0)
        pdf.cell(w=65, h=15, txt='NOMBRES', border=1, align='C', fill=0)
        pdf.cell(w=65, h=15, txt='APELLIDOS', border=1, align='C', fill=0)
        pdf.cell(w=30, h=15, txt='TELEFONO', border=1,ln=1 , align='C', fill=0)

        '''Ingreso de datos de primera tanda'''
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times', '', 10)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        '''funcion .upper() para imprimir de mayusculas los datos ingresados'''
        pdf.cell(w=30, h=15, txt=cedula.upper(), border=1, align='C', fill=0)
        pdf.cell(w=65, h=15, txt=nombres.upper(), border=1, align='C', fill=0)
        pdf.cell(w=65, h=15, txt=apellidos.upper(), border=1, align='C', fill=0)
        pdf.cell(w=30, h=15, txt=celular.upper(), border=1, align='C', fill=0)

        '''Segunda tanda'''
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times', 'B', 12)
        '''funcion ln() para dejar el espaciado de cada celda'''
        pdf.ln(35)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        pdf.cell(w=95, h=15, txt='CALLE PRINCIPAL', border=1, align='C', fill=0)
        pdf.cell(w=95, h=15, txt='CALLE SECUNDARIA', border=1,ln=1 , align='C', fill=0)

        '''Ingreso de datos de segunda tanda'''
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times', '', 10)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        '''funcion .upper() para imprimir de mayusculas los datos ingresados'''
        pdf.cell(w=95, h=15, txt=callePrincipal.upper(), border=1, align='C', fill=0)
        pdf.cell(w=95, h=15, txt=calleSecundaria.upper(), border=1, align='C', fill=0)

        '''Tercera tanda'''
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times', 'B', 12)
        '''funcion ln() para dejar el espaciado de cada celda'''
        pdf.ln(35)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        pdf.multi_cell(w=190, h=15, txt='DESCRIPCION', border=1, align='C', fill=0)

        '''Ingreso de datos de tercera tanda'''
        '''Declaracion de la tipografia, estilo de letra y el tamaño'''
        pdf.set_font('Times', '', 10)
        '''ingreso de texto especificando el X y Y de donde sera ubicado el mensaje o texto'''
        '''funcion .upper() para imprimir de mayusculas los datos ingresados'''
        pdf.multi_cell(w=190, h=5, txt=descripcion.upper(), border=1, align='C', fill=0)

        '''Agregar imagenes, o logos'''
        pdf.image('../../Desktop/ProyectoPoo/logo.png',
                x=80 , y= 220,
                w=60 , h=45)

        '''funcion output con el nombre del archivo para imprimir la informacion en el documento'''
        idPersona=guardarNombrePdf(cedula)
        pdf.output('../../Desktop/ProyectoPoo/RegistrosDescargados/'+"Reporte_"+nombres+idPersona)
def guardarNombrePdf(idPersona):
    nombreTotal=idPersona+".pdf"
    return nombreTotal
if __name__ == '__main__':
        cedula=input("Ingrese du Id: ")
        nombres=input("Ingrese el nombre: ")
        apellidos=input("Ingrese su apellido: ")
        celular=input("Ingrese su numero de celular: ")
        callePrincipal=input("Ingrese la calle principal: ")
        calleSecundaria=input("Ingrese la calle secundaria: ")
        descripcion=input("Ingrese la descripcion: ")
        pdf(cedula, nombres, apellidos, celular, callePrincipal, calleSecundaria, descripcion)
