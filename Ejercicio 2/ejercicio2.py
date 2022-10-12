from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

#1. Al seleccionar un número en el comboCaras,y presionar el botón Tirar Dado el programa debería hacer
# una tirada al azar de un dado de esa cantidad de caras.
#2. El resultado de la tirada debería mostrarse en labelCaras.
  
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicio2.ui", self)
    
app = QApplication([])
win = MiVentana()
win.show()
app.exec_()