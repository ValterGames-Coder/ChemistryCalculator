# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window5.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window4(object):
    def setupUi(self, Window4):
        Window4.setObjectName("Window4")
        Window4.setEnabled(True)
        Window4.resize(500, 400)
        Window4.setMinimumSize(QtCore.QSize(400, 150))
        Window4.setMaximumSize(QtCore.QSize(1000, 1000))
        self.verticalLayout = QtWidgets.QVBoxLayout(Window4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Window4)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(Window4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(Window4)
        self.label.setMinimumSize(QtCore.QSize(450, 280))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Window4)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Window4)
        QtCore.QMetaObject.connectSlotsByName(Window4)

    def retranslateUi(self, Window4):
        _translate = QtCore.QCoreApplication.translate
        Window4.setWindowTitle(_translate("Window4", "Генерация рисунка органического вещества"))
        self.lineEdit.setPlaceholderText(_translate("Window4", "Введите название вещества:"))
        self.pushButton_2.setText(_translate("Window4", "Сгенерировать схему"))
        self.label_2.setText(_translate("Window4", "TextLabel"))
