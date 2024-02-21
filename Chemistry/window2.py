# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window1(object):
    def setupUi(self, Window1):
        Window1.setObjectName("Window1")
        Window1.resize(570, 150)
        Window1.setMinimumSize(QtCore.QSize(400, 150))
        Window1.setMaximumSize(QtCore.QSize(1000, 150))
        self.verticalLayout = QtWidgets.QVBoxLayout(Window1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Window1)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Window1)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Window1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Window1)
        QtCore.QMetaObject.connectSlotsByName(Window1)

    def retranslateUi(self, Window1):
        _translate = QtCore.QCoreApplication.translate
        Window1.setWindowTitle(_translate("Window1", "Относительная молекулярная масса вещества"))
        self.lineEdit.setPlaceholderText(_translate("Window1", "Введите формулу вещества:"))
        self.pushButton.setText(_translate("Window1", "Назад"))
        self.pushButton_2.setText(_translate("Window1", "Получить ответ"))
