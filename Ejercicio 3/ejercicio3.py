from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

#1. Se deberá ingresar un texto en editTexto.
#2. Al presionar el botón calcular deberá cambiar labelLetras por la cantidad de letras
# de ese texto y labelPalabras por la cantidad de palabras del mismo texto.
  
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicio3.ui", self)
    
app = QApplication([])
win = MiVentana()
win.show()
app.exec_()