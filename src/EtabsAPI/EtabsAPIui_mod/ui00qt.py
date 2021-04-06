'''
Esto funciona usando QMainWindow o QWidget, en la clase donde hereda.
Estrucutura de herencia.

    QMainWindow
        .setWindowTitle()
        .setMinimumSize()
        .setGeometry()
            .width()
            .height()

        QLabel()
            .setStyleSheet()
            .setAlignment(
                Qt
                    .Alignment
                    .AlignCenter
                )

        QLineEdit()
            .setPlaceholderText()
            .setClearButtonEnabled()
            .setGeometry()
            .setMaxLength()
            .setEchoMode(
                QLineEdit
                    .EchoMode
                        .NoEcho
                        .Password
                )
            .setReadOnly()

        QPushButton()
            .setGeometry()

b: base, h: altura
'''
from PyQt6.QtWidgets import ( 
    QApplication, QMainWindow, QWidget,
    QLabel, QLineEdit, QPushButton
    )
from PyQt6.QtCore import (
    Qt
    )

class VenPrincipal(QMainWindow): # QWidget
    """docstring for VenPrincipal"""
    def __init__(self, parent=None, *arg):
        super(VenPrincipal, self).__init__(parent=parent)
        
        self.setWindowTitle("Titulo de la Ventana")
        self.setMinimumSize(500, 300)
        # Optenemos la base/largo y altura/ancho, en este caso de QMainWindow
        base = self.frameGeometry().width()
        altura = self.frameGeometry().height()
        print(f"{base},{altura}\n")

        lbl = QLabel("Mi Etiqueta:", self)
        lbl.setStyleSheet("background:#424242; color:#fff")
        lbl.setAlignment(Qt.Alignment.AlignCenter) #| Centrar el texto dentro del Label
        print(f"{lbl.frameGeometry().width(), lbl.frameGeometry().height()}")

        self.eti0 = QLineEdit(self)
        self.eti0.setPlaceholderText("Campo de entrada de datos")
        self.eti0.setClearButtonEnabled(True)  #| crea un boton dentro de TextEdit
        self.eti0.setGeometry(103,2,200,30) # define posicion de la TextEdit
        self.eti0.setMaxLength(30) #| define maximo de 30 letras
        

        self.eti1 = QLineEdit(self)
        self.eti1.setPlaceholderText("Campo de clave")
        self.eti1.setGeometry(103,34,200,30) # define posicion de la TextEdit
        self.eti1.setEchoMode(QLineEdit.EchoMode.Password)

        self.eti2 = QLineEdit(self)
        self.eti2.setPlaceholderText("texto no visible")
        self.eti2.setGeometry(103,66,200,30) # define posicion de la TextEdit
        self.eti2.setEchoMode(QLineEdit.EchoMode.NoEcho)

        self.eti3 = QLineEdit("no editable",self)
        self.eti3.setGeometry(103,98,200,30) # define posicion de la TextEdit
        self.eti3.setReadOnly(True)

        self.btn = QPushButton("Enviar",self)
        self.btn.setGeometry(103,130,200,30)

        # ---------------- triggers | disparadores ------------------
        # self.eti0.returnPressed.connect(self.mostrarDatos)
        self.btn.clicked.connect(self.mostrarDatos)

    def mostrarDatos(self, e):
        print(self.eti0.text())
        print(self.eti1.text())
        print(self.eti2.text())
        print(self.eti3.text())

if __name__ == '__main__':
    import sys
    app = QApplication([]) #| inicia la aplicacion

    ventana = VenPrincipal() #| instancia a la ventana principal
    ventana.show()  #| muestra la ventana, porque por defecto esta oculto.

    sys.exit(app.exec())  #| ejecuta 