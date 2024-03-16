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
        Window4.resize(500, 517)
        Window4.setMinimumSize(QtCore.QSize(400, 150))
        Window4.setMaximumSize(QtCore.QSize(1000, 1000))
        self.gridLayout = QtWidgets.QGridLayout(Window4)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Window4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Window4)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(450, 0))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView = QtWebKitWidgets.QWebView(self.tab_2)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Window4)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.retranslateUi(Window4)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window4)

    def retranslateUi(self, Window4):
        _translate = QtCore.QCoreApplication.translate
        Window4.setWindowTitle(_translate("Window4", "Генерация рисунка органического вещества"))
        self.pushButton_2.setText(_translate("Window4", "Сгенерировать схему"))
        self.label_2.setText(_translate("Window4", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Window4", "2D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Window4", "3D"))
        self.lineEdit.setPlaceholderText(_translate("Window4", "Введите название вещества:"))
from PyQt5 import QtWebKitWidgets
