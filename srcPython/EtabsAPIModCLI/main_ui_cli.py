import sys, os

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextBrowser, 
    QLineEdit, QVBoxLayout, QWidget
    )
from PyQt6.QtGui import QIcon
import constants as cts
import coreapi.menu as cmenu
# exit(dir(cts))

class Window(QWidget): # QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle(cts.c_title_)
        self.setGeometry(cts.c_top_, cts.c_left_, cts.c_width_, cts.c_height_)
        if os.path.isfile(cts.c_appicon_):
            self.setWindowIcon(QIcon(cts.c_appicon_))

        self.initUI()

    def initUI(self):
        self.browser = QTextBrowser() # label que muestra la informacion
        self.lineEdit = QLineEdit("", placeholderText="Entrada de Comando")
        # , statusTip="New model define."
        # "Type An Expression And Hit Enter"
        vbox = QVBoxLayout()
        vbox.addWidget(self.browser)
        vbox.addWidget(self.lineEdit)
        self.setLayout(vbox)

        self.lineEdit.returnPressed.connect(self.updateBrowser)

    def updateBrowser(self):
        try:
            text  = str(self.lineEdit.text())
            self.browser.append("<font color ='#caa451' >%s</font> <b>%s</b>" %(text, eval(text)))
        except:
            self.browser.append("<font color = red > %s Is Invalid </font>" %text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Windows...")
    del(app)