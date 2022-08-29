'''Libreria para la creacion de interface'''
from PyQt5 import QtCore, QtGui, QtWidgets
'''Usando un archivo de la misma carpeta como libreria'''
from ConexionesBD.ConexiónBaseDatos import *
'''Libreria para la creacion de pdf'''
from creaciónPdf.creacionPDF import *
'''Usando un archivo de la misma carpeta como libreria'''
from Validaciones.validaciones import *

class Ui_MenuCallCenter(object):
        '''
        Clase para crear una interfaz grafica que hereda de object
        -------------
        Metodos:
                def setupUi(self, MenuCallCenter, usuario, contrasenia):
                        Metodo para realizar la creacion de la interza gráfica.
                        Esta lleno de funciones de validaciones, creacion de botones, colores, etc.

                def enviarReporte(self):
                        Método que me permite reescribir un usuario, modificando el suarios existente 
                        con el reporte nuevo que se ha creado.

                def descargarPdf2(self) :
                        Metodo que envia los parametros necesarios para la creacion del reporte en pdf.
                        Pasa por parametro todos los datos y esta validado.

                def funcionPrevisualizar(self):
                        método que previsualiza datos que pide datos dinamicos y estaticos. 
                        tambien hace uso de funciones para extraer datos

                def funcionBuscar(self):
                        Metodo para buscar un perfil o un usuario dentro de la interfaz grafica mediante querys
                        Tambien conecta con mongoDB para hacer el uso de datos llamados 

                def funcionBuscar2(self)
                        Metodo para buscar un perfil o un usuario dentro de la interfaz grafica mediante querys
                        Tambien conecta con mongoDB para hacer el uso de datos llamados 

                def retranslateUi(self, MenuCallCenter):
                        Metodo que tranladaba fatos haciendo el uso de funciones para ingrear en en el pdf
                        con las variables correspondientes...

        ------------------
        Variables:
                MenuCallCenter: str
                usuario:str
                contrasenia:str
                
        '''
        def setupUi(self, MenuCallCenter, usuario, contrasenia, acceso):
                '''
                def setupUi(self, MenuCallCenter, usuario, contrasenia):
                        Metodo para realizar la creacion de la interza gráfica.
                        Permite dar el formato de estilo a la ventana principal.
                Parametros:
                ---------------
                        MenuCallCenter: str
                                Propiedades de la ventana principal
                        usuario:str
                                Información de usuario
                        contrasenia:str
                                Contraseña del usuario
                        acceso:str
                                Tipo de acceso que mantendrá el usuario
                '''
                self.contrasenia=contrasenia
                self.usuario=usuario
                MenuCallCenter.setObjectName("MenuCallCenter")
                MenuCallCenter.resize(826, 600)
                self.centralwidget = QtWidgets.QWidget(MenuCallCenter)
                self.centralwidget.setObjectName("centralwidget")
                self.MenuGeneral = QtWidgets.QTabWidget(self.centralwidget)
                self.MenuGeneral.setEnabled(True)
                self.MenuGeneral.setGeometry(QtCore.QRect(10, 10, 781, 571))
                self.MenuGeneral.setTabBarAutoHide(False)
                self.MenuGeneral.setObjectName("MenuGeneral")
                self.OpcionBuscarReporte = QtWidgets.QWidget()
                if acceso== True:
                        self.OpcionBuscarReporte.setEnabled(True)
                else:
                        self.OpcionBuscarReporte.setEnabled(False)
                self.OpcionBuscarReporte.setObjectName("OpcionBuscarReporte")
                self.BotonBuscar = QtWidgets.QPushButton(self.OpcionBuscarReporte)
                self.BotonBuscar.setGeometry(QtCore.QRect(420, 480, 231, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonBuscar.setFont(font)
                self.BotonBuscar.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.BotonBuscar.setObjectName("BotonBuscar")
                self.NombreAdmin = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.NombreAdmin.setGeometry(QtCore.QRect(60, 30, 151, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.NombreAdmin.setFont(font)
                self.NombreAdmin.setObjectName("NombreAdmin")
                self.IdAdministrador = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.IdAdministrador.setGeometry(QtCore.QRect(410, 30, 121, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.IdAdministrador.setFont(font)
                self.IdAdministrador.setObjectName("IdAdministrador")
                self.label_18 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_18.setGeometry(QtCore.QRect(420, 220, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_18.setFont(font)
                self.label_18.setObjectName("label_18")
                self.cajaCaso_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaCaso_2.setEnabled(False)
                self.cajaCaso_2.setGeometry(QtCore.QRect(420, 240, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCaso_2.setFont(font)
                self.cajaCaso_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCaso_2.setObjectName("cajaCaso_2")
                self.label_19 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_19.setGeometry(QtCore.QRect(60, 320, 161, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_19.setFont(font)
                self.label_19.setObjectName("label_19")
                self.label_20 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_20.setGeometry(QtCore.QRect(60, 270, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_20.setFont(font)
                self.label_20.setObjectName("label_20")
                self.label_21 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_21.setGeometry(QtCore.QRect(420, 170, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_21.setFont(font)
                self.label_21.setObjectName("label_21")
                self.cajaNombre_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaNombre_2.setEnabled(False)
                self.cajaNombre_2.setGeometry(QtCore.QRect(60, 240, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaNombre_2.setFont(font)
                self.cajaNombre_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaNombre_2.setObjectName("cajaNombre_2")
                self.cajaTelefono_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaTelefono_2.setEnabled(False)
                self.cajaTelefono_2.setGeometry(QtCore.QRect(60, 290, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaTelefono_2.setFont(font)
                self.cajaTelefono_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaTelefono_2.setObjectName("cajaTelefono_2")
                self.cajaObservaciones_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaObservaciones_2.setEnabled(False)
                self.cajaObservaciones_2.setGeometry(QtCore.QRect(420, 290, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaObservaciones_2.setFont(font)
                self.cajaObservaciones_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaObservaciones_2.setObjectName("cajaObservaciones_2")
                self.cajaICiudad_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaICiudad_2.setEnabled(False)
                self.cajaICiudad_2.setGeometry(QtCore.QRect(60, 340, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaICiudad_2.setFont(font)
                self.cajaICiudad_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaICiudad_2.setObjectName("cajaICiudad_2")
                self.label_22 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_22.setGeometry(QtCore.QRect(420, 270, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_22.setFont(font)
                self.label_22.setObjectName("label_22")
                self.cajaId_3 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaId_3.setGeometry(QtCore.QRect(60, 140, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaId_3.setFont(font)
                self.cajaId_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaId_3.setObjectName("cajaId_3")
                self.cajaAvenida_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaAvenida_2.setEnabled(False)
                self.cajaAvenida_2.setGeometry(QtCore.QRect(60, 400, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaAvenida_2.setFont(font)
                self.cajaAvenida_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaAvenida_2.setObjectName("cajaAvenida_2")
                self.cajaApellido_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaApellido_2.setEnabled(False)
                self.cajaApellido_2.setGeometry(QtCore.QRect(60, 190, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaApellido_2.setFont(font)
                self.cajaApellido_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaApellido_2.setObjectName("cajaApellido_2")
                self.label_23 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_23.setGeometry(QtCore.QRect(60, 120, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_23.setFont(font)
                self.label_23.setObjectName("label_23")
                self.label_24 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_24.setGeometry(QtCore.QRect(60, 170, 91, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_24.setFont(font)
                self.label_24.setObjectName("label_24")
                self.cajaCallePrincipal_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaCallePrincipal_2.setEnabled(False)
                self.cajaCallePrincipal_2.setGeometry(QtCore.QRect(420, 140, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCallePrincipal_2.setFont(font)
                self.cajaCallePrincipal_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCallePrincipal_2.setObjectName("cajaCallePrincipal_2")
                self.label_25 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_25.setGeometry(QtCore.QRect(420, 120, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_25.setFont(font)
                self.label_25.setObjectName("label_25")
                self.label_26 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_26.setGeometry(QtCore.QRect(60, 380, 171, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_26.setFont(font)
                self.label_26.setObjectName("label_26")
                self.label_27 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.label_27.setGeometry(QtCore.QRect(60, 220, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_27.setFont(font)
                self.label_27.setObjectName("label_27")
                self.cajaCalleSecundaria_2 = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.cajaCalleSecundaria_2.setEnabled(False)
                self.cajaCalleSecundaria_2.setGeometry(QtCore.QRect(420, 190, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCalleSecundaria_2.setFont(font)
                self.cajaCalleSecundaria_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCalleSecundaria_2.setObjectName("cajaCalleSecundaria_2")
                self.BotonBuscar_2 = QtWidgets.QPushButton(self.OpcionBuscarReporte)
                self.BotonBuscar_2.setGeometry(QtCore.QRect(150, 480, 231, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonBuscar_2.setFont(font)
                self.BotonBuscar_2.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.BotonBuscar_2.setObjectName("BotonBuscar_2")
                self.CajaNombrAdmin = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.CajaNombrAdmin.setEnabled(False)
                self.CajaNombrAdmin.setGeometry(QtCore.QRect(210, 30, 161, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.CajaNombrAdmin.setFont(font)
                self.CajaNombrAdmin.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.CajaNombrAdmin.setObjectName("CajaNombrAdmin")
                mongo=MongoDb("sistema911", "localhost", "27017", 1000)
                IdAdministrador=usuario
                listaUsuario=mongo.buscarId(mongo.conectar(), "usuarios", int(IdAdministrador))
                self.CajaNombrAdmin.setText(listaUsuario[0]["usuario"])
                self.CajaIdAdmin = QtWidgets.QLineEdit(self.OpcionBuscarReporte)
                self.CajaIdAdmin.setEnabled(False)
                self.CajaIdAdmin.setGeometry(QtCore.QRect(540, 30, 191, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.CajaIdAdmin.setFont(font)
                self.CajaIdAdmin.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.CajaIdAdmin.setObjectName("CajaIdAdmin")
                self.CajaIdAdmin.setText(usuario)
                self.labelError1 = QtWidgets.QLabel(self.OpcionBuscarReporte)
                self.labelError1.setGeometry(QtCore.QRect(440, 380, 181, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelError1.setFont(font)
                self.labelError1.setStyleSheet("QLabel{\n"
        "    color:#D91818;\n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.labelError1.setText("")
                self.labelError1.setObjectName("labelError1")
                self.MenuGeneral.addTab(self.OpcionBuscarReporte, "")
                self.OpcionAniadirReporte = QtWidgets.QWidget()
                if acceso== True:
                        self.OpcionAniadirReporte.setEnabled(True)
                else:
                        self.OpcionAniadirReporte.setEnabled(False)
                self.OpcionAniadirReporte.setObjectName("OpcionAniadirReporte")
                self.BotonSituacion = QtWidgets.QPushButton(self.OpcionAniadirReporte)
                self.BotonSituacion.setGeometry(QtCore.QRect(310, 470, 211, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonSituacion.setFont(font)
                self.BotonSituacion.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.BotonSituacion.setObjectName("BotonSituacion")
                self.label = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label.setGeometry(QtCore.QRect(80, 90, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_2.setGeometry(QtCore.QRect(80, 140, 91, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_3.setGeometry(QtCore.QRect(80, 190, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_4.setGeometry(QtCore.QRect(80, 240, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_5.setGeometry(QtCore.QRect(80, 290, 161, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_6.setGeometry(QtCore.QRect(80, 350, 171, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_6.setFont(font)
                self.label_6.setObjectName("label_6")
                self.cajaId = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaId.setGeometry(QtCore.QRect(80, 110, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaId.setFont(font)
                self.cajaId.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaId.setObjectName("cajaId")
                self.BotonSituacion_2 = QtWidgets.QPushButton(self.OpcionAniadirReporte)
                self.BotonSituacion_2.setGeometry(QtCore.QRect(560, 470, 211, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonSituacion_2.setFont(font)
                self.BotonSituacion_2.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.BotonSituacion_2.setObjectName("BotonSituacion_2")
                self.cajaApellido = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaApellido.setEnabled(False)
                self.cajaApellido.setGeometry(QtCore.QRect(80, 160, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaApellido.setFont(font)
                self.cajaApellido.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                self.cajaApellido.setObjectName("cajaApellido")
                self.cajaNombre = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaNombre.setEnabled(False)
                self.cajaNombre.setGeometry(QtCore.QRect(80, 210, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaNombre.setFont(font)
                self.cajaNombre.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaNombre.setObjectName("cajaNombre")
                self.cajaTelefono = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaTelefono.setEnabled(True)
                self.cajaTelefono.setGeometry(QtCore.QRect(80, 260, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaTelefono.setFont(font)
                self.cajaTelefono.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaTelefono.setObjectName("cajaTelefono")
                self.cajaICiudad = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaICiudad.setEnabled(True)
                self.cajaICiudad.setGeometry(QtCore.QRect(80, 310, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaICiudad.setFont(font)
                self.cajaICiudad.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaICiudad.setObjectName("cajaICiudad")
                self.cajaAvenida = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaAvenida.setGeometry(QtCore.QRect(80, 370, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaAvenida.setFont(font)
                self.cajaAvenida.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaAvenida.setObjectName("cajaAvenida")
                self.label_13 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_13.setGeometry(QtCore.QRect(290, 20, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_13.setFont(font)
                self.label_13.setObjectName("label_13")
                self.cajaCallePrincipal = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaCallePrincipal.setGeometry(QtCore.QRect(440, 100, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCallePrincipal.setFont(font)
                self.cajaCallePrincipal.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                self.cajaCallePrincipal.setObjectName("cajaCallePrincipal")
                self.label_14 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_14.setGeometry(QtCore.QRect(440, 80, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_14.setFont(font)
                self.label_14.setObjectName("label_14")
                self.cajaCalleSecundaria = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaCalleSecundaria.setGeometry(QtCore.QRect(440, 150, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCalleSecundaria.setFont(font)
                self.cajaCalleSecundaria.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCalleSecundaria.setObjectName("cajaCalleSecundaria")
                self.label_15 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_15.setGeometry(QtCore.QRect(440, 130, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_15.setFont(font)
                self.label_15.setObjectName("label_15")
                self.cajaCaso = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaCaso.setGeometry(QtCore.QRect(440, 200, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCaso.setFont(font)
                self.cajaCaso.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCaso.setObjectName("cajaCaso")
                self.label_16 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_16.setGeometry(QtCore.QRect(440, 180, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_16.setFont(font)
                self.label_16.setObjectName("label_16")
                self.label_17 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.label_17.setGeometry(QtCore.QRect(440, 230, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_17.setFont(font)
                self.label_17.setObjectName("label_17")
                self.cajaObservaciones = QtWidgets.QLineEdit(self.OpcionAniadirReporte)
                self.cajaObservaciones.setGeometry(QtCore.QRect(440, 250, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaObservaciones.setFont(font)
                self.cajaObservaciones.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaObservaciones.setObjectName("cajaObservaciones")
                self.BotonSituacion_3 = QtWidgets.QPushButton(self.OpcionAniadirReporte)
                self.BotonSituacion_3.setGeometry(QtCore.QRect(60, 470, 211, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonSituacion_3.setFont(font)
                self.BotonSituacion_3.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.BotonSituacion_3.setObjectName("BotonSituacion_3")
                self.labelError2 = QtWidgets.QLabel(self.OpcionAniadirReporte)
                self.labelError2.setGeometry(QtCore.QRect(450, 370, 181, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelError2.setFont(font)
                self.labelError2.setStyleSheet("QLabel{\n"
        "    color:#D91818;\n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.labelError2.setText("")
                self.labelError2.setObjectName("labelError2")
                self.MenuGeneral.addTab(self.OpcionAniadirReporte, "")
                self.OpcionEliminarReporte = QtWidgets.QWidget()
                if acceso== True:
                        self.OpcionEliminarReporte.setEnabled(True)
                else:
                        self.OpcionEliminarReporte.setEnabled(False)
                self.OpcionEliminarReporte.setObjectName("OpcionEliminarReporte")
                self.cajaCalleSecundaria_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)

                self.cajaCalleSecundaria_3.setEnabled(False)
                self.cajaCalleSecundaria_3.setGeometry(QtCore.QRect(450, 200, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCalleSecundaria_3.setFont(font)
                self.cajaCalleSecundaria_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCalleSecundaria_3.setObjectName("cajaCalleSecundaria_3")
                self.cajaCallePrincipal_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaCallePrincipal_3.setEnabled(False)
                self.cajaCallePrincipal_3.setGeometry(QtCore.QRect(450, 150, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCallePrincipal_3.setFont(font)
                self.cajaCallePrincipal_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCallePrincipal_3.setObjectName("cajaCallePrincipal_3")
                self.cajaApellido_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaApellido_3.setEnabled(False)
                self.cajaApellido_3.setGeometry(QtCore.QRect(90, 200, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaApellido_3.setFont(font)
                self.cajaApellido_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaApellido_3.setObjectName("cajaApellido_3")
                self.cajaTelefono_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaTelefono_3.setEnabled(False)
                self.cajaTelefono_3.setGeometry(QtCore.QRect(90, 300, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaTelefono_3.setFont(font)
                self.cajaTelefono_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaTelefono_3.setObjectName("cajaTelefono_3")
                self.label_28 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_28.setGeometry(QtCore.QRect(450, 230, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_28.setFont(font)
                self.label_28.setObjectName("label_28")
                self.label_8 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_8.setGeometry(QtCore.QRect(90, 280, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_8.setFont(font)
                self.label_8.setObjectName("label_8")
                self.label_12 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_12.setGeometry(QtCore.QRect(90, 230, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_12.setFont(font)
                self.label_12.setObjectName("label_12")
                self.cajaId_2 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaId_2.setGeometry(QtCore.QRect(90, 150, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaId_2.setFont(font)
                self.cajaId_2.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaId_2.setObjectName("cajaId_2")
                self.cajaObservaciones_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaObservaciones_3.setEnabled(False)
                self.cajaObservaciones_3.setGeometry(QtCore.QRect(450, 300, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaObservaciones_3.setFont(font)
                self.cajaObservaciones_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaObservaciones_3.setObjectName("cajaObservaciones_3")
                self.label_30 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_30.setGeometry(QtCore.QRect(450, 280, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_30.setFont(font)
                self.label_30.setObjectName("label_30")
                self.label_29 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_29.setGeometry(QtCore.QRect(450, 180, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_29.setFont(font)
                self.label_29.setObjectName("label_29")
                self.cajaCaso_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaCaso_3.setEnabled(False)
                self.cajaCaso_3.setGeometry(QtCore.QRect(450, 250, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCaso_3.setFont(font)
                self.cajaCaso_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCaso_3.setObjectName("cajaCaso_3")
                self.cajaICiudad_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaICiudad_3.setEnabled(False)
                self.cajaICiudad_3.setGeometry(QtCore.QRect(90, 350, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaICiudad_3.setFont(font)
                self.cajaICiudad_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaICiudad_3.setObjectName("cajaICiudad_3")
                self.label_9 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_9.setGeometry(QtCore.QRect(90, 130, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_9.setFont(font)
                self.label_9.setObjectName("label_9")
                self.label_11 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_11.setGeometry(QtCore.QRect(90, 390, 171, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_11.setFont(font)
                self.label_11.setObjectName("label_11")
                self.label_31 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_31.setGeometry(QtCore.QRect(450, 130, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_31.setFont(font)
                self.label_31.setObjectName("label_31")
                self.label_10 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_10.setGeometry(QtCore.QRect(90, 180, 91, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_10.setFont(font)
                self.label_10.setObjectName("label_10")
                self.cajaNombre_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaNombre_3.setEnabled(False)
                self.cajaNombre_3.setGeometry(QtCore.QRect(90, 250, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaNombre_3.setFont(font)
                self.cajaNombre_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaNombre_3.setObjectName("cajaNombre_3")
                self.cajaAvenida_3 = QtWidgets.QLineEdit(self.OpcionEliminarReporte)
                self.cajaAvenida_3.setEnabled(False)
                self.cajaAvenida_3.setGeometry(QtCore.QRect(90, 410, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaAvenida_3.setFont(font)
                self.cajaAvenida_3.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaAvenida_3.setObjectName("cajaAvenida_3")
                self.label_7 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_7.setGeometry(QtCore.QRect(90, 330, 161, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_7.setFont(font)
                self.label_7.setObjectName("label_7")
                self.label_32 = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.label_32.setGeometry(QtCore.QRect(290, 20, 191, 31))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_32.setFont(font)
                self.label_32.setObjectName("label_32")
                self.BotonSituacion_4 = QtWidgets.QPushButton(self.OpcionEliminarReporte)
                self.BotonSituacion_4.setGeometry(QtCore.QRect(310, 470, 211, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonSituacion_4.setFont(font)
                self.BotonSituacion_4.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.BotonSituacion_4.setObjectName("BotonSituacion_4")
                self.BotonSituacion_5 = QtWidgets.QPushButton(self.OpcionEliminarReporte)
                self.BotonSituacion_5.setGeometry(QtCore.QRect(560, 470, 211, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonSituacion_5.setFont(font)
                self.BotonSituacion_5.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.BotonSituacion_5.setObjectName("BotonSituacion_5")
                self.BotonSituacion_6 = QtWidgets.QPushButton(self.OpcionEliminarReporte)
                self.BotonSituacion_6.setGeometry(QtCore.QRect(60, 470, 211, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonSituacion_6.setFont(font)
                self.BotonSituacion_6.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.BotonSituacion_6.setObjectName("BotonSituacion_6")
                self.labelError = QtWidgets.QLabel(self.OpcionEliminarReporte)
                self.labelError.setGeometry(QtCore.QRect(450, 370, 181, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelError.setFont(font)
                self.labelError.setStyleSheet("QLabel{\n"
        "    color:#D91818;\n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.labelError.setText("")
                self.labelError.setObjectName("labelError")
                self.MenuGeneral.addTab(self.OpcionEliminarReporte, "")
                self.OpcionDescargarPdf = QtWidgets.QWidget()
                if acceso==True:
                        self.OpcionDescargarPdf.setEnabled(True)
                else:
                        self.OpcionDescargarPdf.setEnabled(True)
                self.OpcionDescargarPdf.setObjectName("OpcionDescargarPdf")
                self.cajaCalleSecundaria_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaCalleSecundaria_4.setEnabled(False)
                self.cajaCalleSecundaria_4.setGeometry(QtCore.QRect(420, 190, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCalleSecundaria_4.setFont(font)
                self.cajaCalleSecundaria_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCalleSecundaria_4.setObjectName("cajaCalleSecundaria_4")
                self.label_33 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_33.setGeometry(QtCore.QRect(60, 170, 91, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_33.setFont(font)
                self.label_33.setObjectName("label_33")
                self.cajaCallePrincipal_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaCallePrincipal_4.setEnabled(False)
                self.cajaCallePrincipal_4.setGeometry(QtCore.QRect(420, 140, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCallePrincipal_4.setFont(font)
                self.cajaCallePrincipal_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCallePrincipal_4.setObjectName("cajaCallePrincipal_4")
                self.cajaTelefono_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaTelefono_4.setEnabled(False)
                self.cajaTelefono_4.setGeometry(QtCore.QRect(60, 290, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaTelefono_4.setFont(font)
                self.cajaTelefono_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                self.cajaTelefono_4.setObjectName("cajaTelefono_4")
                self.labelError4 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.labelError4.setGeometry(QtCore.QRect(440, 380, 181, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelError4.setFont(font)
                self.labelError4.setStyleSheet("QLabel{\n"
        "    color:#D91818;\n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.labelError4.setText("")
                self.labelError4.setObjectName("labelError4")
                self.label_34 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_34.setGeometry(QtCore.QRect(420, 220, 81, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_34.setFont(font)
                self.label_34.setObjectName("label_34")
                self.cajaApellido_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaApellido_4.setEnabled(False)
                self.cajaApellido_4.setGeometry(QtCore.QRect(60, 190, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaApellido_4.setFont(font)
                self.cajaApellido_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaApellido_4.setObjectName("cajaApellido_4")
                self.label_35 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_35.setGeometry(QtCore.QRect(60, 270, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_35.setFont(font)
                self.label_35.setObjectName("label_35")
                self.cajaCaso_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaCaso_4.setEnabled(False)
                self.cajaCaso_4.setGeometry(QtCore.QRect(420, 240, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaCaso_4.setFont(font)
                self.cajaCaso_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaCaso_4.setObjectName("cajaCaso_4")
                self.cajaObservaciones_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaObservaciones_4.setEnabled(False)
                self.cajaObservaciones_4.setGeometry(QtCore.QRect(420, 290, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaObservaciones_4.setFont(font)
                self.cajaObservaciones_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaObservaciones_4.setObjectName("cajaObservaciones_4")
                self.label_36 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_36.setGeometry(QtCore.QRect(60, 220, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_36.setFont(font)
                self.label_36.setObjectName("label_36")
                self.cajaAvenida_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaAvenida_4.setEnabled(False)
                self.cajaAvenida_4.setGeometry(QtCore.QRect(60, 400, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaAvenida_4.setFont(font)
                self.cajaAvenida_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaAvenida_4.setObjectName("cajaAvenida_4")
                self.cajaNombre_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaNombre_4.setEnabled(False)
                self.cajaNombre_4.setGeometry(QtCore.QRect(60, 240, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaNombre_4.setFont(font)
                self.cajaNombre_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaNombre_4.setObjectName("cajaNombre_4")
                self.label_37 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_37.setGeometry(QtCore.QRect(60, 380, 171, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_37.setFont(font)
                self.label_37.setObjectName("label_37")
                self.label_38 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_38.setGeometry(QtCore.QRect(60, 320, 161, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_38.setFont(font)
                self.label_38.setObjectName("label_38")
                self.label_39 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_39.setGeometry(QtCore.QRect(420, 270, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_39.setFont(font)
                self.label_39.setObjectName("label_39")
                self.cajaId_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaId_4.setGeometry(QtCore.QRect(60, 140, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaId_4.setFont(font)
                self.cajaId_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaId_4.setObjectName("cajaId_4")
                self.label_40 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_40.setGeometry(QtCore.QRect(420, 170, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_40.setFont(font)
                self.label_40.setObjectName("label_40")
                self.label_41 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_41.setGeometry(QtCore.QRect(60, 120, 91, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_41.setFont(font)
                self.label_41.setObjectName("label_41")
                self.label_42 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_42.setGeometry(QtCore.QRect(420, 120, 121, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_42.setFont(font)
                self.label_42.setObjectName("label_42")
                self.cajaICiudad_4 = QtWidgets.QLineEdit(self.OpcionDescargarPdf)
                self.cajaICiudad_4.setEnabled(False)
                self.cajaICiudad_4.setGeometry(QtCore.QRect(60, 340, 211, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.cajaICiudad_4.setFont(font)
                self.cajaICiudad_4.setStyleSheet("QLineEdit{\n"
        "background: transparent;color:#E84040;border:none;border-bottom:1px solid #756D6D;\n"
        "}\n"
        "")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.cajaICiudad_4.setObjectName("cajaICiudad_4")
                self.PrevisualizarDatos = QtWidgets.QPushButton(self.OpcionDescargarPdf)
                self.PrevisualizarDatos.setGeometry(QtCore.QRect(310, 470, 211, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.PrevisualizarDatos.setFont(font)
                self.PrevisualizarDatos.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                self.PrevisualizarDatos.setObjectName("PrevisualizarDatos")
                self.BotonSituacion_8 = QtWidgets.QPushButton(self.OpcionDescargarPdf)
                self.BotonSituacion_8.setGeometry(QtCore.QRect(60, 470, 211, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.BotonSituacion_8.setFont(font)
                self.BotonSituacion_8.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones para agregar nombres a los botones, agregarle tamañano y altura,
                Validaciones de botones, el tipo de fuente, etc.'''
                '''Asignacion de un nombre a un boton'''
                self.BotonSituacion_8.setObjectName("BotonSituacion_8")
                '''asignacion a una variable para generar un boton para descargar el pdf o reporte'''
                self.descargarPdf = QtWidgets.QPushButton(self.OpcionDescargarPdf)
                self.descargarPdf.setGeometry(QtCore.QRect(560, 470, 211, 41))
                '''Asignaciones de funtes con int y boolean'''
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.descargarPdf.setFont(font)
                '''metodo para descargar el pdf o reporte'''
                self.descargarPdf.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                '''Funciones con self para presionar botones y asignar funciones a los mismos'''
                self.descargarPdf.setObjectName("descargarPdf")
                self.label_43 = QtWidgets.QLabel(self.OpcionDescargarPdf)
                self.label_43.setGeometry(QtCore.QRect(290, 20, 161, 31))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_43.setFont(font)
                self.label_43.setObjectName("label_43")
                self.MenuGeneral.addTab(self.OpcionDescargarPdf, "")
                MenuCallCenter.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MenuCallCenter)
                self.statusbar.setEnabled(True)
                self.statusbar.setObjectName("statusbar")
                MenuCallCenter.setStatusBar(self.statusbar)
                '''Funciones con self para presionar botones y asignar funciones a los mismos'''
                self.retranslateUi(MenuCallCenter)
                self.MenuGeneral.setCurrentIndex(3)
                self.BotonSituacion_6.clicked.connect(self.cajaCaso_3.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaObservaciones_2.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaNombre.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaApellido_2.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaCalleSecundaria.clear)  
                self.BotonSituacion_6.clicked.connect(self.cajaICiudad_3.clear)  
                self.BotonSituacion_5.clicked.connect(self.cajaAvenida_3.copy)  
                self.BotonBuscar_2.clicked.connect(self.cajaICiudad_2.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaId_3.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaICiudad.clear)  
                self.BotonSituacion_6.clicked.connect(self.cajaId_2.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaAvenida.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaCaso.clear)  
                self.BotonSituacion_6.clicked.connect(self.cajaTelefono_3.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaNombre_2.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaId.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaTelefono.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaTelefono_2.clear)  
                self.BotonBuscar.clicked.connect(self.cajaId_3.copy)  
                self.BotonSituacion_3.clicked.connect(self.cajaCallePrincipal.clear)  
                self.BotonSituacion_6.clicked.connect(self.cajaAvenida_3.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaCaso_2.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaAvenida_2.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaApellido.clear)  
                self.BotonSituacion_4.clicked.connect(self.cajaId_2.copy)  
                self.BotonSituacion_6.clicked.connect(self.cajaNombre_3.clear)  
                self.BotonSituacion_3.clicked.connect(self.cajaObservaciones.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaCalleSecundaria_2.clear)   
                self.BotonSituacion_6.clicked.connect(self.cajaApellido_3.clear)  
                self.BotonBuscar_2.clicked.connect(self.cajaCallePrincipal_2.clear)  
                self.BotonSituacion_6.clicked.connect(self.cajaObservaciones_3.clear)   
                self.BotonSituacion_6.clicked.connect(self.cajaCalleSecundaria_3.clear)  
                self.BotonSituacion_6.clicked.connect(self.cajaCallePrincipal_3.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaId_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaApellido_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaNombre_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaTelefono_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaICiudad_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaAvenida_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaCallePrincipal_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaCalleSecundaria_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaCaso_4.clear)  
                self.BotonSituacion_8.clicked.connect(self.cajaObservaciones_4.clear)  
                QtCore.QMetaObject.connectSlotsByName(MenuCallCenter)
                #--------------------------------------------------------
                #                        EVENTOS
                #--------------------------------------------------------
                self.BotonSituacion.clicked.connect(self.funcionBuscar) 
                self.BotonBuscar.clicked.connect(self.funcionBuscar2)
                self.PrevisualizarDatos.clicked.connect(self.funcionPrevisualizar)
                self.descargarPdf.clicked.connect(self.descargarPdf2)
                self.BotonSituacion_2.clicked.connect(self.enviarReporte)
                self.BotonSituacion_4.clicked.connect(self.eliminarReporte)
                self.BotonSituacion_5.clicked.connect(self.eliminarReporte2)
        def eliminarReporte2(self):
                '''
                def eliminarReporte2(self):
                        Método que envía los datos obtenidos del buscar a un diccionario y lo envia a la función de enviarReporte
                Métodos
                --------
                        -enviarReporte()                
                -----------
                Atributos
                        cedula:int
                        nombre:str
                        apellido:str
                        telefono:str
                        ciudad:str
                        avenida:str
                        callePrincipal: str
                        calleSecundaria: str
                        caso: str
                        observaciones: str
                ---------
                '''
                conectarMongo=MongoDb("sistema911","localhost", "27017", 1000)
                cedula=int(self.cajaId_2.text())
                nombre=self.cajaNombre_3.text()
                apellido=self.cajaApellido_3.text()
                telefono=self.cajaTelefono_3.text()
                ciudad=self.cajaICiudad_3.text()
                avenida=self.cajaAvenida_3.text()
                callePrincipal=self.cajaCallePrincipal_3.text()
                calleSecundaria=self.cajaCalleSecundaria_3.text()
                caso=""
                observaciones=""
                try:            
                        '''Query de como se ingresaran los datos dentro del mongo db con las variables''' 
                        rol=conectarMongo.buscarId(conectarMongo.conectar(), "roles", int(cedula)) 
                        documento={"_id":cedula,"nombre":nombre,"apellido":apellido,"telefono":telefono,"direccion":ciudad,"avenida":avenida,"callePrincipal":callePrincipal,"calleSecundaria":calleSecundaria,"caso":caso,"observaciones":observaciones, "usuario":"", "contrasenia":"", "roles":rol}                
                        actualizar=conectarMongo.actualizarUsuario(conectarMongo.conectar(), "usuarios", documento, cedula)
                        if actualizar==True:                                
                                self.labelError.setText("Se ha actualizado el usuario")
                        else:
                                self.labelError.setText("Error al actualizar")
                except:
                        print("Error al enviar el reporte")
        def eliminarReporte(self):
                conectarMongo=MongoDb("sistema911","localhost", "27017", 1000)
                cedula=int(self.cajaId_2.text())
                IdEncontrada=conectarMongo.buscarId(conectarMongo.conectar(),"usuarios", cedula)
                self.cajaApellido_3.setText(IdEncontrada[0]["apellido"])
                self.cajaNombre_3.setText(IdEncontrada[0]["nombre"])
                self.cajaTelefono_3.setText(IdEncontrada[0]["telefono"])
                self.cajaICiudad_3.setText(IdEncontrada[0]["direccion"])
                self.cajaAvenida_3.setText(IdEncontrada[0]["avenida"])
                self.cajaId_3.setText(str(IdEncontrada[0]["_id"]))
                self.cajaCallePrincipal_3.setText(IdEncontrada[0]["callePrincipal"])
                self.cajaCalleSecundaria_3.setText(IdEncontrada[0]["calleSecundaria"])
                self.cajaCaso_3.setText(IdEncontrada[0]["caso"])
                self.cajaObservaciones_3.setText(IdEncontrada[0]["observaciones"])


        def enviarReporte(self):
                '''
                def enviarReporte(self):
                        Método que envía los datos obtenidos del buscar a un diccionario y lo envia a la función de enviarReporte
                Métodos
                --------
                        -enviarReporte()                
                -----------
                Atributos
                        cedula:int
                        nombre:str
                        apellido:str
                        telefono:str
                        ciudad:str
                        avenida:str
                        callePrincipal: str
                        calleSecundaria: str
                        caso: str
                        observaciones: str
                ---------
                '''
                conectarMongo=MongoDb("sistema911","localhost", "27017", 1000)
                cedula=int(self.cajaId.text())
                nombre=self.cajaNombre.text()
                apellido=self.cajaApellido.text()
                telefono=self.cajaTelefono.text()
                ciudad=self.cajaICiudad.text()
                avenida=self.cajaAvenida.text()
                callePrincipal=self.cajaCallePrincipal.text()
                calleSecundaria=self.cajaCalleSecundaria.text()
                caso=self.cajaCaso.text()
                observaciones=self.cajaObservaciones.text()
                try:            
                        '''Query de como se ingresaran los datos dentro del mongo db con las variables'''
                        usuario=conectarMongo.buscarId(conectarMongo.conectar(), "usuarios", int(cedula)) 
                        casoAnterior=usuario[0]["caso"]
                        observacionesAnteriores=usuario[0]["observaciones"]
                        actualizar=conectarMongo.actualizarUsuario2(conectarMongo.conectar(), "usuarios", cedula,casoAnterior, caso, observacionesAnteriores, observaciones)
                        '''Validacion para saber si se a actualizado o no'''
                        if actualizar==True:                                
                                self.labelError2.setText("Se ha actualizado el usuario")
                        else:
                                self.labelError2.setText("Error al actualizar")
                except:
                        print("Error al enviar el reporte")
        def descargarPdf2(self) :
                '''Metodo  para descar el reporte 
                --------------
                variables:
                        id:str
                        nombre:str
                        apellido:str
                        telefono:str
                        ciudad:str
                        avenida:str
                        callePrincipal:str
                        calleSecundaria:str
                        caso:str
                        observaciones:str

                '''
                nombre=self.cajaNombre_4.text()
                '''Validacion con if y else'''
                if validarDatoVacio(nombre)==False:
                        self.labelError4.setText("ERROR AL DESCARGAR")
                else:   
                        '''Ingreso de datos dinamicos con str y variables estaticas'''
                        id=str(self.cajaId_4.text())
                        nombre=self.cajaNombre_4.text()
                        apellido=self.cajaApellido_4.text()
                        telefono=self.cajaTelefono_4.text()
                        ciudad=self.cajaICiudad_4.text()
                        avenida=self.cajaAvenida_4.text()
                        callePrincipal=self.cajaCallePrincipal_4.text()
                        calleSecundaria=self.cajaCalleSecundaria_4.text()
                        caso=self.cajaCaso_4.text()
                        observaciones=self.cajaObservaciones_4.text()
                        '''Paso de variables por parametro para la creacion del reporte o pdf'''
                        pdf(id, nombre, apellido,telefono, callePrincipal, calleSecundaria, caso)
        def funcionPrevisualizar(self):
                '''
                def funcionPrevisualizar(self):
                        Método que envía los datos obtenidos del buscar a un diccionario y lo envia a la función de enviarReporte
                '''
                try:
                        '''Ingreso de dato de manera dinamica y de tipo numerico'''
                        id=int(self.cajaId_4.text())
                        '''conectar con la base de datos o coleccion de mongoDB'''
                        conectarMongo=MongoDb("sistema911", "localhost", "27017", 1000)
                        IdEncontrada=conectarMongo.buscarId(conectarMongo.conectar(),"usuarios",id)
                        '''Llamando a funciones para que devuelva datos '''
                        self.cajaApellido_4.setText(IdEncontrada[0]["apellido"])
                        self.cajaNombre_4.setText(IdEncontrada[0]["nombre"])
                        self.cajaTelefono_4.setText(IdEncontrada[0]["telefono"])
                        self.cajaICiudad_4.setText(IdEncontrada[0]["direccion"])
                        self.cajaAvenida_4.setText(IdEncontrada[0]["avenida"])
                        self.cajaCallePrincipal_4.setText(IdEncontrada[0]["callePrincipal"])
                        self.cajaCalleSecundaria_4.setText(IdEncontrada[0]["calleSecundaria"])
                        self.cajaCaso_4.setText(IdEncontrada[0]["caso"])
                        self.cajaObservaciones_4.setText(IdEncontrada[0]["observaciones"])
                except:
                        self.labelError4.setText("Error al previsualizar los datos")

        def funcionBuscar(self):
                '''Metodo para buscar un perfil o un usuario dentro de la interfaz grafica mediante querys '''
                try: 
                        '''Ingreso de dato dinamico de tipo numerico'''
                        id=int(self.cajaId.text())
                        '''Funcion para conectar con la base de datos'''
                        conectarMongo=MongoDb("sistema911", "localhost", "27017", 1000)
                        '''Instanciacion'''
                        IdEncontrada=conectarMongo.buscarId(conectarMongo.conectar(), "usuarios", id)
                        '''Llamado a los datos '''
                        self.cajaApellido.setText(IdEncontrada[0]['apellido'])
                        self.cajaNombre.setText(IdEncontrada[0]['nombre'])
                        self.cajaTelefono.setText(IdEncontrada[0]['telefono'])
                        self.cajaICiudad.setText(IdEncontrada[0]['direccion'])
                        self.cajaAvenida.setText(IdEncontrada[0]['avenida'])
                        self.cajaObservaciones.setText(IdEncontrada[0]['observaciones'])
                        self.cajaCaso.setText(IdEncontrada[0]['caso'])
                        self.cajaCalleSecundaria.setText(IdEncontrada[0]['calleSecundaria'])
                        self.cajaCallePrincipal.setText(IdEncontrada[0]['callePrincipal'])
                except:
                        self.labelError2.setText("NO EXISTE EN LA BASE DE DATOS")

        def funcionBuscar2(self):
                '''Funcion para buscar un usuario o un cliente con sus respectivos datos'''
                try:
                        '''ingreso de dato dinamico de tipo numerico'''
                        id=int(self.cajaId_3.text())
                        '''Funcion para conectar con MongoDB'''
                        conectarMongo=MongoDb("sistema911", "localhost", "27017", 1000)
                        IdEncontrada=conectarMongo.buscarId(conectarMongo.conectar(),"usuarios",id)
                        '''Llamado de datos para que busque '''
                        self.cajaApellido_2.setText((IdEncontrada)[0]['nombre'])
                        self.cajaNombre_2.setText(IdEncontrada[0]['apellido'])
                        self.cajaTelefono_2.setText(IdEncontrada[0]['telefono'])
                        self.cajaICiudad_2.setText(IdEncontrada[0]['direccion'])
                        self.cajaAvenida_2.setText(IdEncontrada[0]['avenida'])
                        self.cajaCallePrincipal_2.setText(IdEncontrada[0]['callePrincipal'])
                        self.cajaCalleSecundaria_2.setText(IdEncontrada[0]['calleSecundaria'])
                        self.cajaCaso_2.setText(IdEncontrada[0]['caso'])
                        self.cajaObservaciones_2.setText(IdEncontrada[0]['observaciones'])
                except:
                        self.labelError1.setText("NO EXISTE EN LA BASE DE DATOS")


        def retranslateUi(self, MenuCallCenter):
                '''Trasladacion de datos'''
                _translate = QtCore.QCoreApplication.translate
                MenuCallCenter.setWindowTitle(_translate("MenuCallCenter", "CallCenter"))
                '''Llamando a funciones '''
                self.BotonBuscar.setText(_translate("MenuCallCenter", "Buscar"))
                self.NombreAdmin.setText(_translate("MenuCallCenter", "Nombre Administrador"))
                self.IdAdministrador.setText(_translate("MenuCallCenter", "ID Administrador:"))
                self.label_18.setText(_translate("MenuCallCenter", "Caso"))
                self.label_19.setText(_translate("MenuCallCenter", "Ciudad"))
                self.label_20.setText(_translate("MenuCallCenter", "Telefono"))
                self.label_21.setText(_translate("MenuCallCenter", "Calle Secundaria"))
                self.label_22.setText(_translate("MenuCallCenter", "Observaciones"))
                self.label_23.setText(_translate("MenuCallCenter", "ID/ Cédula"))
                self.label_24.setText(_translate("MenuCallCenter", "Apellido"))
                self.label_25.setText(_translate("MenuCallCenter", "Calle principal"))
                self.label_26.setText(_translate("MenuCallCenter", "Avenida"))
                self.label_27.setText(_translate("MenuCallCenter", "Nombre"))
                self.BotonBuscar_2.setText(_translate("MenuCallCenter", "Limpiar Reporte"))
                '''Llamando a funciones '''
                self.MenuGeneral.setTabText(self.MenuGeneral.indexOf(self.OpcionBuscarReporte), _translate("MenuCallCenter", "Buscar Reporte"))
                self.BotonSituacion.setText(_translate("MenuCallCenter", "Buscar"))
                self.label.setText(_translate("MenuCallCenter", "ID/ Cédula"))
                self.label_2.setText(_translate("MenuCallCenter", "Apellido"))
                self.label_3.setText(_translate("MenuCallCenter", "Nombre"))
                self.label_4.setText(_translate("MenuCallCenter", "Telefono"))
                self.label_5.setText(_translate("MenuCallCenter", "Ciudad"))
                self.label_6.setText(_translate("MenuCallCenter", "Avenida"))
                self.BotonSituacion_2.setText(_translate("MenuCallCenter", "Agregar"))
                self.label_13.setText(_translate("MenuCallCenter", "Agregar informe"))
                self.label_14.setText(_translate("MenuCallCenter", "Calle principal"))
                self.label_15.setText(_translate("MenuCallCenter", "Calle Secundaria"))
                self.label_16.setText(_translate("MenuCallCenter", "Caso"))
                self.label_17.setText(_translate("MenuCallCenter", "Observaciones"))
                self.BotonSituacion_3.setText(_translate("MenuCallCenter", "Limpiar Campos"))
                '''Llamando a funciones '''
                self.MenuGeneral.setTabText(self.MenuGeneral.indexOf(self.OpcionAniadirReporte), _translate("MenuCallCenter", "Añadir Reporte"))
                self.label_28.setText(_translate("MenuCallCenter", "Caso"))
                self.label_8.setText(_translate("MenuCallCenter", "Telefono"))
                self.label_12.setText(_translate("MenuCallCenter", "Nombre"))
                self.label_30.setText(_translate("MenuCallCenter", "Observaciones"))
                self.label_29.setText(_translate("MenuCallCenter", "Calle Secundaria"))
                self.label_9.setText(_translate("MenuCallCenter", "ID/ Cédula"))
                self.label_11.setText(_translate("MenuCallCenter", "Avenida"))
                self.label_31.setText(_translate("MenuCallCenter", "Calle principal"))
                self.label_10.setText(_translate("MenuCallCenter", "Apellido"))
                self.label_7.setText(_translate("MenuCallCenter", "Ciudad"))
                self.label_32.setText(_translate("MenuCallCenter", "Eliminar Reporte"))
                self.BotonSituacion_4.setText(_translate("MenuCallCenter", "Buscar"))
                self.BotonSituacion_5.setText(_translate("MenuCallCenter", "Eliminar"))
                self.BotonSituacion_6.setText(_translate("MenuCallCenter", "Limpiar Campos"))
                '''Llamando a funciones '''
                self.MenuGeneral.setTabText(self.MenuGeneral.indexOf(self.OpcionEliminarReporte), _translate("MenuCallCenter", "Eliminar Reporte"))
                self.label_33.setText(_translate("MenuCallCenter", "Apellido"))
                self.label_34.setText(_translate("MenuCallCenter", "Caso"))
                self.label_35.setText(_translate("MenuCallCenter", "Telefono"))
                self.label_36.setText(_translate("MenuCallCenter", "Nombre"))
                self.label_37.setText(_translate("MenuCallCenter", "Avenida"))
                self.label_38.setText(_translate("MenuCallCenter", "Ciudad"))
                self.label_39.setText(_translate("MenuCallCenter", "Observaciones"))
                self.label_40.setText(_translate("MenuCallCenter", "Calle Secundaria"))
                self.label_41.setText(_translate("MenuCallCenter", "ID/ Cédula"))
                self.label_42.setText(_translate("MenuCallCenter", "Calle principal"))
                self.PrevisualizarDatos.setText(_translate("MenuCallCenter", "Previsualizar Datos"))
                self.BotonSituacion_8.setText(_translate("MenuCallCenter", "Limpiar Campos"))
                self.descargarPdf.setText(_translate("MenuCallCenter", "Descargar PDF"))
                self.label_43.setText(_translate("MenuCallCenter", "Descargar Pdf"))
                '''Llamando a funciones '''
                self.MenuGeneral.setTabText(self.MenuGeneral.indexOf(self.OpcionDescargarPdf), _translate("MenuCallCenter", "DescargarRegistro"))
if __name__ == "__main__":
        '''Importacion de libreria sys'''
        import sys
        '''Instanciacion '''
        app = QtWidgets.QApplication(sys.argv)
        MenuCallCenter = QtWidgets.QMainWindow()
        ui = Ui_MenuCallCenter()
        '''llamado de funciones con datos estaticos'''
        ui.setupUi(MenuCallCenter)
        '''Mostrar en la interfaz grafica'''
        MenuCallCenter.show()
        '''Metodo que permite cerrar una ventana'''
        sys.exit(app.exec_())
