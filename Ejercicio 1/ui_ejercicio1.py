# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jgracia/Desktop/ejercicios-pyqt5/Ejercicio 1/ejercicio1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 139)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botonMultiplicar = QtWidgets.QPushButton(self.centralwidget)
        self.botonMultiplicar.setGeometry(QtCore.QRect(260, 30, 91, 33))
        self.botonMultiplicar.setObjectName("botonMultiplicar")
        self.comboMultiplicador = QtWidgets.QComboBox(self.centralwidget)
        self.comboMultiplicador.setGeometry(QtCore.QRect(10, 30, 241, 31))
        self.comboMultiplicador.setObjectName("comboMultiplicador")
        self.comboMultiplicador.addItem("")
        self.comboMultiplicador.addItem("")
        self.comboMultiplicador.addItem("")
        self.comboMultiplicador.addItem("")
        self.comboMultiplicador.addItem("")
        self.labelCinco = QtWidgets.QLabel(self.centralwidget)
        self.labelCinco.setGeometry(QtCore.QRect(10, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelCinco.setFont(font)
        self.labelCinco.setObjectName("labelCinco")
        self.labelCombo = QtWidgets.QLabel(self.centralwidget)
        self.labelCombo.setGeometry(QtCore.QRect(80, 80, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelCombo.setFont(font)
        self.labelCombo.setObjectName("labelCombo")
        self.labelIgual = QtWidgets.QLabel(self.centralwidget)
        self.labelIgual.setGeometry(QtCore.QRect(120, 80, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelIgual.setFont(font)
        self.labelIgual.setObjectName("labelIgual")
        self.labelResultado = QtWidgets.QLabel(self.centralwidget)
        self.labelResultado.setGeometry(QtCore.QRect(160, 80, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelResultado.setFont(font)
        self.labelResultado.setObjectName("labelResultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botonMultiplicar.setText(_translate("MainWindow", "Multiplicar"))
        self.comboMultiplicador.setItemText(0, _translate("MainWindow", "1"))
        self.comboMultiplicador.setItemText(1, _translate("MainWindow", "2"))
        self.comboMultiplicador.setItemText(2, _translate("MainWindow", "3"))
        self.comboMultiplicador.setItemText(3, _translate("MainWindow", "4"))
        self.comboMultiplicador.setItemText(4, _translate("MainWindow", "5"))
        self.labelCinco.setText(_translate("MainWindow", "5 x"))
        self.labelCombo.setText(_translate("MainWindow", "1"))
        self.labelIgual.setText(_translate("MainWindow", "="))
        self.labelResultado.setText(_translate("MainWindow", "5"))
