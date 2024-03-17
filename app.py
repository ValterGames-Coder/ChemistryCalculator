from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QUrl
from chemlib import Compound

from deep_translator import GoogleTranslator
from mendeleev import mendeleev
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw.MolDrawing import DrawingOptions
from urllib.request import urlopen

DrawingOptions.includeAtomNumbers = True

translated = GoogleTranslator(source='auto', target='en')


class Ui_MainMenu(object):

    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(400, 350)
        MainMenu.setMinimumSize(QtCore.QSize(400, 350))
        MainMenu.setMaximumSize(QtCore.QSize(1000, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainMenu.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        MainMenu.setCentralWidget(self.centralwidget)

        MainMenu.setWindowTitle("Chemistry Calculator")
        self.pushButton.setText("Относительная молекулярная масса вещества")
        self.pushButton_2.setText("Массовая доля вещества")
        self.pushButton_3.setText("Расчет необходимой массы вещества для реакции")
        self.pushButton_4.setText("Генерация рисунка органического вещества")
        #QtCore.QMetaObject.connectSlotsByName(MainMenu)

        self.w1 = Ui_Window1()
        self.w2 = Ui_Window2()
        self.w3 = Ui_Window3()
        self.w4 = Ui_Window4()
        self.pushButton.clicked.connect(lambda: self.show_new_window(self.w1))
        self.pushButton_2.clicked.connect(lambda: self.show_new_window(self.w2))
        self.pushButton_3.clicked.connect(lambda: self.show_new_window(self.w3))
        self.pushButton_4.clicked.connect(lambda: self.show_new_window(self.w4))

    def show_new_window(self, window):
        self.widget = QtWidgets.QWidget()
        window.setupUi(self.widget)
        self.widget.show()


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
        self.pushButton_2 = QtWidgets.QPushButton(Window1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Window1.setWindowTitle("Относительная молекулярная масса вещества")
        self.lineEdit.setPlaceholderText("Введите форxулу вещества:")
        self.pushButton_2.setText("Получить ответ")
        #QtCore.QMetaObject.connectSlotsByName(Window1)
        self.pushButton_2.clicked.connect(self.result)

    def result(self):
        try:
            compound = Compound(self.lineEdit.text())
            result = QMessageBox()
            result.setWindowTitle('Результат')
            result.setText('Ответ: ' + '%.0f' % compound.molar_mass())
            result.setStandardButtons(QMessageBox.Ok)

            result.exec()
        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setIcon(QMessageBox.Warning)
            error.setText('Неправильно введена формула')

            error.exec()


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
        self.pushButton_2 = QtWidgets.QPushButton(Window2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        Window2.setWindowTitle("Массовая доля вещества")
        self.lineEdit_2.setPlaceholderText("Введите формулу вещества:")
        self.lineEdit.setPlaceholderText("Введите атом:")
        self.pushButton_2.setText("Получить ответ")
        #QtCore.QMetaObject.connectSlotsByName(Window2)

        self.pushButton_2.clicked.connect(self.result)

    def result(self):
        try:
            compound = Compound(self.lineEdit_2.text())
            atom = self.lineEdit.text()
            result = QMessageBox()
            result.setWindowTitle('Результат')
            result.setText('Ответ: ' + '%.0f' % compound.percentage_by_mass(atom) + '%')
            result.setStandardButtons(QMessageBox.Ok)

            result.exec()
        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setIcon(QMessageBox.Warning)
            error.setText('Неправильно введена формула')

            error.exec()


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
        self.pushButton_2 = QtWidgets.QPushButton(Window3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        #QtCore.QMetaObject.connectSlotsByName(Window3)

        self.pushButton_2.clicked.connect(self.result)

        Window3.setWindowTitle("Расчет необходимой массы вещества для реакции")
        self.lineEdit_2.setPlaceholderText("Введите формулу вещества:")
        self.lineEdit.setPlaceholderText("Введите атом")
        self.lineEdit_3.setPlaceholderText("Введите массу атома")
        self.pushButton_2.setText("Получить ответ")

    def result(self):
        try:
            compound = Compound(self.lineEdit_2.text())
            mass = int(self.lineEdit_3.text())
            atom = mendeleev.element(self.lineEdit.text())
            result = QMessageBox()
            result.setWindowTitle('Результат')
            result.setText('Ответ: ' + '%.0f' % (mass / (compound.percentage_by_mass(atom.symbol) / 100)) + 'г.')
            result.setStandardButtons(QMessageBox.Ok)

            result.exec()
        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setIcon(QMessageBox.Warning)
            error.setText('Неправильно введена формула')

            error.exec()


class Ui_Window4(object):
    def setupUi(self, Window4):
        Window4.setObjectName("Window4")
        Window4.setEnabled(True)
        Window4.resize(500, 500)
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
        self.webView = QWebEngineView(self.tab_2)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.webView.setMinimumSize(QtCore.QSize(300, 300))
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

        self.tabWidget.setCurrentIndex(0)
        #QtCore.QMetaObject.connectSlotsByName(Window4)

        self.pushButton_2.clicked.connect(lambda: self.generate_image(self.lineEdit.text()))

        Window4.setWindowTitle("Генерация рисунка органического вещества")
        self.pushButton_2.setText("Сгенерировать схему")
        self.label_2.setText("Химическая формула")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),"2D")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "3D")
        self.lineEdit.setPlaceholderText( "Введите название вещества:")

    def generate_image(self, text):
        try:
            # name = text
            print(text)
            name = translated.translate(str(text))
            # name = name.replace(' ', '')
            print(name)
            url = 'https://cactus.nci.nih.gov/chemical/structure/' + name + '/smiles'
            ans = urlopen(url).read().decode('utf8')
            url = 'https://cactus.nci.nih.gov/chemical/structure/' + name + '/formula'
            formula = urlopen(url).read().decode('utf8')
            url = 'https://cactus.nci.nih.gov/chemical/structure/' + name + '/twirl'
            html = urlopen(url).read().decode('utf8')

            size = (self.label.geometry().size().width(), self.label.geometry().size().height())
            str(html).replace('700', str(self.label.geometry().size().width()))
            str(html).replace('1000', str(self.label.geometry().size().width()))
            m = Chem.MolFromSmiles(ans)

            for atom in m.GetAtoms():
                if atom.GetNumImplicitHs() > 1:
                    atom.SetProp("atomLabel", f'{atom.GetSymbol()}H{atom.GetNumImplicitHs()}')
                elif atom.GetNumImplicitHs() == 1:
                    atom.SetProp("atomLabel", f'{atom.GetSymbol()}H')
                else:
                    atom.SetProp("atomLabel", f'{atom.GetSymbol()}')

            fig = Draw.MolToImage(m, size=size)
            fig.save('img.png')
            self.pixmap = QPixmap('img.png')
            self.label.setPixmap(self.pixmap)
            self.label_2.setText(formula)
            self.webView.load(QUrl(url))
            self.webView.show()
        except:
            self.pixmap = QPixmap('error.png')
            self.label.setPixmap(self.pixmap)
            self.label_2.setText('Ошибка')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())