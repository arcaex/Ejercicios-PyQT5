from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

#1. Al seleccionar un número en el comboMultiplicar, debería cambiar el labelCombo por ese número seleccionado.
#2. Al presionar el botón Multiplicar, debería cambiar el labelResultado que es 5 multiplicado por el valor
# seleccionado en el comboMultiplicar.
  
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ejercicio1.ui", self)
    

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()