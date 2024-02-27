# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window2(object):
    def setupUi(self, Window2):
        Window2.setObjectName("Window2")
        Window2.resize(563, 200)
        Window2.setMinimumSize(QtCore.QSize(400, 200))
        Window2.setMaximumSize(QtCore.QSize(1000, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(Window2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(Window2)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(Window2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Window2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Window2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "Массовая доля вещества"))
        self.lineEdit_2.setPlaceholderText(_translate("Window2", "Введите формулу вещества:"))
        self.lineEdit.setPlaceholderText(_translate("Window2", "Введите атом:"))
        self.pushButton.setText(_translate("Window2", "Назад"))
        self.pushButton_2.setText(_translate("Window2", "Получить ответ"))
