from concurrent.futures.thread import BrokenThreadPool
from re import *
import random as r
from ConexionesBD.ConexiónBaseDatos import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Validaciones.validaciones import *
class Ui_Registro(object):
        def setupUi(self, Registro):
                Registro.setObjectName("Registro")
                Registro.resize(789, 653)
                self.ventanaRegistro = QtWidgets.QWidget(Registro)
                self.ventanaRegistro.setObjectName("ventanaRegistro")
                self.botonIniciar = QtWidgets.QPushButton(self.ventanaRegistro)
                self.botonIniciar.setGeometry(QtCore.QRect(300, 530, 191, 41))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.botonIniciar.setFont(font)
                self.botonIniciar.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                self.botonIniciar.setObjectName("botonIniciar")
                self.botonRegistrar = QtWidgets.QPushButton(self.ventanaRegistro)
                self.botonRegistrar.setGeometry(QtCore.QRect(300, 580, 191, 41))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.botonRegistrar.setFont(font)
                self.botonRegistrar.setStyleSheet("QPushButton{\n"
        "    border-radius:20px;\n"
        "    background:transparent;\n"
        "    border: 2px solid #C61B1B\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background:#D91818;\n"
        "color:black;        \n"
        "    \n"
        "}")
                self.botonRegistrar.setObjectName("botonRegistrar")
                self.labeLogo = QtWidgets.QLabel(self.ventanaRegistro)
                self.labeLogo.setGeometry(QtCore.QRect(285, 60,190, 130))
                self.labeLogo.setText("")
                self.labeLogo.setPixmap(QtGui.QPixmap("../../Desktop/ProyectoPoo/logo.png"))
                self.labeLogo.setScaledContents(True)
                self.labeLogo.setObjectName("labeLogo")
                self.labelUsuario = QtWidgets.QLabel(self.ventanaRegistro)
                self.labelUsuario.setGeometry(QtCore.QRect(110, 250, 71, 31))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelUsuario.setFont(font)
                self.labelUsuario.setObjectName("labelUsuario")
                self.labelContrasenia = QtWidgets.QLabel(self.ventanaRegistro)
                self.labelContrasenia.setGeometry(QtCore.QRect(440, 251, 71, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelContrasenia.setFont(font)
                self.labelContrasenia.setObjectName("labelContrasenia")
                self.cajaUsuario = QtWidgets.QLineEdit(self.ventanaRegistro)
                self.cajaUsuario.setGeometry(QtCore.QRect(110, 280, 241, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.cajaUsuario.setFont(font)
                self.cajaUsuario.setStyleSheet("QLineEdit{\n"
        "background: transparent;\n"
        "color:#E84040;\n"
        "border:none;\n"
        "border-bottom:1px solid #756D6D;\n"
        "}")
                self.cajaUsuario.setObjectName("cajaUsuario")
                self.cajaContrasenia = QtWidgets.QLineEdit(self.ventanaRegistro)
                self.cajaContrasenia.setGeometry(QtCore.QRect(440, 280, 241, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.cajaContrasenia.setFont(font)
                self.cajaContrasenia.setStyleSheet("QLineEdit{\n"
        "background: transparent;\n"
        "color:#E84040;\n"
        "border:none;\n"
        "border-bottom:1px solid #756D6D;\n"
        "}")
                self.cajaContrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
                self.cajaContrasenia.setObjectName("cajaContrasenia")
                self.labelError = QtWidgets.QLabel(self.ventanaRegistro)
                self.labelError.setGeometry(QtCore.QRect(330, 470, 141, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelError.setFont(font)
                self.labelError.setStyleSheet("color:#E84040;")
                self.labelError.setText("")
                self.labelError.setObjectName("labelError")
                self.labelNombre = QtWidgets.QLabel(self.ventanaRegistro)
                self.labelNombre.setGeometry(QtCore.QRect(110, 320, 71, 31))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelNombre.setFont(font)
                self.labelNombre.setObjectName("labelNombre")
                self.cajaNombre = QtWidgets.QLineEdit(self.ventanaRegistro)
                self.cajaNombre.setGeometry(QtCore.QRect(110, 350, 241, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.cajaNombre.setFont(font)
                self.cajaNombre.setStyleSheet("QLineEdit{\n"
        "background: transparent;\n"
        "color:#E84040;\n"
        "border:none;\n"
        "border-bottom:1px solid #756D6D;\n"
        "}")
                self.cajaNombre.setObjectName("cajaNombre")
                self.cajaApellido = QtWidgets.QLineEdit(self.ventanaRegistro)
                self.cajaApellido.setGeometry(QtCore.QRect(440, 350, 241, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.cajaApellido.setFont(font)
                self.cajaApellido.setStyleSheet("QLineEdit{\n"
        "background: transparent;\n"
        "color:#E84040;\n"
        "border:none;\n"
        "border-bottom:1px solid #756D6D;\n"
        "}")
                self.cajaApellido.setObjectName("cajaApellido")
                self.labelApellido = QtWidgets.QLabel(self.ventanaRegistro)
                self.labelApellido.setGeometry(QtCore.QRect(440, 320, 71, 31))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelApellido.setFont(font)
                self.labelApellido.setObjectName("labelApellido")
                self.cajaEmail = QtWidgets.QLineEdit(self.ventanaRegistro)
                self.cajaEmail.setGeometry(QtCore.QRect(110, 420, 241, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.cajaEmail.setFont(font)
                self.cajaEmail.setStyleSheet("QLineEdit{\n"
        "background: transparent;\n"
        "color:#E84040;\n"
        "border:none;\n"
        "border-bottom:1px solid #756D6D;\n"
        "}")
                self.cajaEmail.setObjectName("cajaEmail")
                self.labelEmail = QtWidgets.QLabel(self.ventanaRegistro)
                self.labelEmail.setGeometry(QtCore.QRect(110, 390, 71, 31))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelEmail.setFont(font)
                self.labelEmail.setObjectName("labelEmail")
                self.labelError_2 = QtWidgets.QLabel(self.ventanaRegistro)
                self.labelError_2.setGeometry(QtCore.QRect(470, 430, 181, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelError_2.setFont(font)
                self.labelError_2.setText("")
                self.labelError_2.setObjectName("labelError_2")
                self.cajaCedula = QtWidgets.QLineEdit(self.ventanaRegistro)
                self.cajaCedula.setGeometry(QtCore.QRect(440, 420, 241, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.cajaCedula.setFont(font)
                self.cajaCedula.setStyleSheet("QLineEdit{\n"
        "background: transparent;\n"
        "color:#E84040;\n"
        "border:none;\n"
        "border-bottom:1px solid #756D6D;\n"
        "}")
                self.cajaCedula.setObjectName("cajaCedula")
                self.labelCedula = QtWidgets.QLabel(self.ventanaRegistro)
                self.labelCedula.setGeometry(QtCore.QRect(440, 390, 71, 31))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelCedula.setFont(font)
                self.labelCedula.setObjectName("labelCedula")
                Registro.setCentralWidget(self.ventanaRegistro)
                self.statusbar = QtWidgets.QStatusBar(Registro)
                self.statusbar.setObjectName("statusbar")
                Registro.setStatusBar(self.statusbar)

                self.retranslateUi(Registro)
                QtCore.QMetaObject.connectSlotsByName(Registro)
                #--------------------------------------------------------
                #                        EVENTOS
                #--------------------------------------------------------
                self.botonRegistrar.clicked.connect(self.registrar)
                self.botonIniciar.clicked.connect(self.iniciar)
        def retranslateUi(self, Registro):
                _translate = QtCore.QCoreApplication.translate
                Registro.setWindowTitle(_translate("Registro", "Ventana Registro"))
                self.botonIniciar.setText(_translate("Registro", "Iniciar Sesión"))
                self.botonRegistrar.setText(_translate("Registro", "Registrarse"))
                self.labelUsuario.setText(_translate("Registro", "Usuario"))
                self.labelContrasenia.setText(_translate("Registro", "Contraseña"))
                self.labelNombre.setText(_translate("Registro", "Nombre"))
                self.labelApellido.setText(_translate("Registro", "Apellido"))
                self.labelEmail.setText(_translate("Registro", "Email"))
                self.labelCedula.setText(_translate("Registro", "Cédula"))
        def iniciar(self, Registro, *args, **kwargs):
                from login import Ui_Login
                import sys
                self.app = QtWidgets.QApplication(sys.argv)
                self.Login = QtWidgets.QMainWindow()
                self.ui = Ui_Login()
                self.ui.setupUi(self.Login)
                self.Login.show()
        def registrar(self):
                '''
                def registrar (self):
                        funcion que me permite registrar un usuario en la base de datos, pasando por una serie de validaciones
                        que me permiten validar que los campos no esten vacios y que el usuario no exista en la base de datos
                Parametros:
                ---------------
                        Ninguno                        
                '''
                acumulador=0                      
                if validarCaracteres(self.cajaUsuario.text())==True:
                        usuario=self.cajaUsuario.text()
                        acumulador=acumulador+1
                else:
                        self.cajaUsuario.setPlaceholderText("Usuario no válida")
                        self.cajaUsuario.setText("")
                if validarContraseña(self.cajaContrasenia.text())==True:
                        contrasenia=self.cajaContrasenia.text()
                        acumulador=acumulador+1
                else:
                        self.cajaContrasenia.setPlaceholderText("Contraseña no válida")
                        self.cajaContrasenia.setText("")
                if validarCaracteres(self.cajaNombre.text())==True:
                        nombre=self.cajaNombre.text()
                        acumulador=acumulador+1
                else:
                        self.cajaNombre.setPlaceholderText("Nombre no válido")
                        self.cajaNombre.setText("")
                if validarCaracteres(self.cajaApellido.text())==True:
                        apellido=self.cajaApellido.text()
                        acumulador=acumulador+1
                else:
                        self.cajaApellido.setPlaceholderText("Apellido no válido")
                        self.cajaApellido.setText("")
                if validarEmail(self.cajaEmail.text())==True:
                        email=self.cajaEmail.text()
                        acumulador=acumulador+1
                else:
                        self.cajaEmail.setPlaceholderText("Email no válido")
                        self.cajaEmail.setText("")
                if validarNumero(self.cajaCedula.text())==True:
                        cedula=int(self.cajaCedula.text())
                        acumulador=acumulador+1
                else:
                        self.cajaCedula.setPlaceholderText("Cédula no válida")
                        self.cajaCedula.setText("")
                if acumulador==6:
                        print("si es igual a 6")
                        conectarMongo=MongoDb("sistema911","localhost","27017",1000)
                        rolnuevo=conectarMongo.buscarId(conectarMongo.conectar(), "roles", 5000)
                        diccionario={"_id":cedula,"nombre":nombre,"apellido":apellido,"telefono":"","direccion":"", "avenida":"","callePrincipal":"","calleSecundaria":"", "caso": "No existe", "observaciones":"No existe", "usuario":usuario, "contrasenia":contrasenia, "roles":rolnuevo}
                        datosGuardados=conectarMongo.guardarUsuario2(conectarMongo.conectar(),"usuarios", diccionario)
                        if datosGuardados==True:
                                self.labelError.setText("Usuario registrado")
                else:
                        self.labelError.setText("Error al registrar")                        
if __name__ == "__main__":
        '''
        if __name__ == "__main__":
                Main principal , que se encarga de iniciar la ventana de registro
        '''
        import sys
        app2 = QtWidgets.QApplication(sys.argv)
        Registro = QtWidgets.QMainWindow()
        ui = Ui_Registro()
        ui.setupUi(Registro)
        Registro.show()
        sys.exit(app2.exec_())
