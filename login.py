from ConexionesBD.buscarUsuarios import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Validaciones.validaciones import *
import sys
class Ui_Login(object):
        '''
        class Ui_Login(object):
                clase que se encarga de la interfaz de login y su correcto funcionamiento, la mayoría de sus 
                propiedades de los métodos forman parte de la interfaz de usuario
        Métodos:
        ----------
        def setupUi(self, Login)
                Método que se encargar de las propiedades de la ventana del login, es decir; el título, el tamaño,diseño, colores
                y demás.
        def retranslateUi(self, Login)
                Método que se encargar de las traducciones de las etiquetas y demás elementos de la interfaz de usuario
        def login(self):
                Método que se encarga de validar el usuario y contraseña obtenidos de la caja de texto
                y validando con la base de datos
        def registrar(self):
                Método que me permite llamar la la ventana de registro y cerra las existente
        Atributsos:
        ----------
                nombreUsuario
                        Contiene el usuario ingresado en la caja de texto
                contrasenia
                        Contiene la contraseña ingresada en la caja de texto
        '''
        def setupUi(self, Login):
                Login.setObjectName("Login")
                Login.resize(368, 600)
                self.ventanaLogin = QtWidgets.QWidget(Login)
                self.ventanaLogin.setObjectName("VentanaLogin")
                self.botonIniciar = QtWidgets.QPushButton(self.ventanaLogin)
                self.botonIniciar.setGeometry(QtCore.QRect(90, 480, 191, 41))
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
                self.botonRegistrar = QtWidgets.QPushButton(self.ventanaLogin)
                self.botonRegistrar.setGeometry(QtCore.QRect(90, 530, 191, 41))
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
                self.labeLogo = QtWidgets.QLabel(self.ventanaLogin)
                self.labeLogo.setGeometry(QtCore.QRect(85, 60, 190, 130))
                self.labeLogo.setText("")
                self.labeLogo.setPixmap(QtGui.QPixmap("../../Desktop/ProyectoPoo/logo.png"))
                self.labeLogo.setScaledContents(True)
                self.labeLogo.setObjectName("labeLogo")
                self.labelUsuario = QtWidgets.QLabel(self.ventanaLogin)
                self.labelUsuario.setGeometry(QtCore.QRect(70, 240, 71, 31))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelUsuario.setFont(font)
                self.labelUsuario.setObjectName("labelUsuario")
                self.labelContrasenia = QtWidgets.QLabel(self.ventanaLogin)
                self.labelContrasenia.setGeometry(QtCore.QRect(70, 341, 71, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelContrasenia.setFont(font)
                self.labelContrasenia.setObjectName("labelContrasenia")
                self.cajaUsuario = QtWidgets.QLineEdit(self.ventanaLogin)
                self.cajaUsuario.setGeometry(QtCore.QRect(70, 280, 241, 20))
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
                self.cajaContrasenia = QtWidgets.QLineEdit(self.ventanaLogin)
                self.cajaContrasenia.setGeometry(QtCore.QRect(70, 370, 241, 20))
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
                self.labelError = QtWidgets.QLabel(self.ventanaLogin)
                self.labelError.setGeometry(QtCore.QRect(100, 430, 181, 20))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Condensed")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.labelError.setFont(font)
                self.labelError.setText("")
                self.labelError.setObjectName("labelError")
                Login.setCentralWidget(self.ventanaLogin)
                self.statusbar = QtWidgets.QStatusBar(Login)
                self.statusbar.setObjectName("statusbar")
                Login.setStatusBar(self.statusbar)
                self.retranslateUi(Login)
                QtCore.QMetaObject.connectSlotsByName(Login)
        def retranslateUi(self, Login):
                _translate = QtCore.QCoreApplication.translate
                Login.setWindowTitle(_translate("Login", "Login Unidad 3"))
                self.botonIniciar.setText(_translate("Login", "Iniciar Sesión"))
                self.botonRegistrar.setText(_translate("Login", "Registrarse"))
                self.labelUsuario.setText(_translate("Login", "Cédula"))
                self.labelContrasenia.setText(_translate("Login", "Contraseña"))
                #--------------------------------------------------------
                #                        EVENTOS
                #--------------------------------------------------------
                self.botonRegistrar.clicked.connect(self.registrar)
                self.botonIniciar.clicked.connect(self.login)
        def login (self):
                '''
                def  login(self);
                        Método que se encarga de validar el usuario y contraseña obtenidos de la caja de texto
                        y validando con la base de datos    
                Atributos
                ----------
                self.cajaUsuario.text()
                        Contiene el usuario ingresado en la caja de texto
                self.cajaContrasenia.text()
                        Contiene la contraseña ingresada en la caja de texto
                '''
                if validarDatoVacio(self.cajaUsuario.text())==False:                                                
                        self.cajaUsuario.setPlaceholderText("No puede dejar campos vacios")
                        self.cajaUsuario.setText("")
                else:
                        usuarioIngreso=self.cajaUsuario.text()
                        contraseniaIngreso=self.cajaContrasenia.text()
                        usuarios=str(retornarUsuarios())
                        contrasenia=retornarContraseñas()
                        if usuarioIngreso in usuarios and contraseniaIngreso in contrasenia:
                                conectarMongo=MongoDb("sistema911", "localhost", "27017", 1000)
                                listaRoles=conectarMongo.retornarIds(conectarMongo.conectar(), "roles")
                                datosUsuario=conectarMongo.buscarId(conectarMongo.conectar(), "usuarios", int(usuarioIngreso))
        
                                IdRolUusario=datosUsuario[0]["roles"][0]["_id"]
                                if IdRolUusario in listaRoles:
                                        if IdRolUusario==5000:
                                                acceso=True
                                                from callCenterFinal import Ui_MenuCallCenter
                                                import sys
                                                self.app = QtWidgets.QApplication(sys.argv)
                                                self.MenuCallCenter = QtWidgets.QMainWindow()
                                                self.ui = Ui_MenuCallCenter()
                                                self.ui.setupUi(self.MenuCallCenter, usuarioIngreso, id,acceso )
                                                self.MenuCallCenter.show()                                 
                                        elif IdRolUusario==5001:
                                                acceso=False
                                                from callCenterFinal import Ui_MenuCallCenter
                                                import sys
                                                self.app = QtWidgets.QApplication(sys.argv)
                                                self.MenuCallCenter = QtWidgets.QMainWindow()
                                                self.ui = Ui_MenuCallCenter()
                                                self.ui.setupUi(self.MenuCallCenter, usuarioIngreso, contraseniaIngreso,acceso )
                                                self.MenuCallCenter.show()    
                                
                                else:
                                        self.labelError.setText("NO EXISTE ESTE ROL")
                        else:
                                self.labelError.setText("Usuario o contraseña incorrectos")
                if validarDatoVacio(self.cajaContrasenia.text())==False:                        
                        self.cajaContrasenia.setPlaceholderText("No puede dejar campos vacios")
                        self.cajaContrasenia.setText("")                        
        def registrar(self):
                '''
                def registrar(self):
                        Método que me permite llamar la la ventana de registro y cerra la existente
                Parámetros
                ----------
                        Ninguno
                '''
                from registro import Ui_Registro
                import sys                
                self.app2 = QtWidgets.QApplication(sys.argv)
                self.Registro = QtWidgets.QMainWindow()
                self.ui = Ui_Registro()
                self.ui.setupUi(self.Registro)
                self.Registro.show()
                Login.close()
if __name__ == "__main__":
        '''
        if __name__ == "__main__":
                Main principal , que se encarga de iniciar la ventana de login, para poder acceder a las 
                otras ventanas que se encuentran en el programa.
        '''
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Login = QtWidgets.QMainWindow()
        ui = Ui_Login()
        ui.setupUi(Login)
        Login.show()
        sys.exit(app.exec_())
