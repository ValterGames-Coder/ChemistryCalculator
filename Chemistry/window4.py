# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window3(object):
    def setupUi(self, Window3):
        Window3.setObjectName("Window3")
        Window3.resize(550, 250)
        Window3.setMinimumSize(QtCore.QSize(400, 250))
        Window3.setMaximumSize(QtCore.QSize(1000, 250))
        self.verticalLayout = QtWidgets.QVBoxLayout(Window3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(Window3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(Window3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(Window3)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Window3)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Window3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Window3)
        QtCore.QMetaObject.connectSlotsByName(Window3)

    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        Window3.setWindowTitle(_translate("Window3", "Расчет необходимой массы вещества для реакции"))
        self.lineEdit_2.setPlaceholderText(_translate("Window3", "Введите формулу вещества:"))
        self.lineEdit.setPlaceholderText(_translate("Window3", "Введите атом"))
        self.lineEdit_3.setPlaceholderText(_translate("Window3", "Введите массу атома"))
        self.pushButton.setText(_translate("Window3", "Назад"))
        self.pushButton_2.setText(_translate("Window3", "Получить ответ"))
