from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from carbonpy import Namer
import translate
from rdkit import Chem
from rdkit.Chem import Draw
from urllib.request import urlopen
from googletrans import Translator
translator = Translator()

ru_translator = translate.Translator(to_lang='russian')
#translator = translate.Translator(to_lang='en', from_lang='russian')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 70, 600, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 130, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 180, 600, 250))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chemistry"))
        self.label.setText(_translate("MainWindow", "Введите формулу:"))
        self.pushButton.setText(_translate("MainWindow", "Сгенерировать"))

    def add_functions(self):
        self.pushButton.clicked.connect(lambda: self.generate_image(self.lineEdit.text()))

    def write_name(self, text):
        try:
            print(text.upper())
            formula = Namer(text.upper()).molecular_formula()
            name = Namer(text.upper()).analyser()
            name = translator.translate(name)
            self.label_2.setText(f'{formula} - {name}')
        except:
            self.label_2.setText('Неправильно введена формула')

    def generate_image(self, text):
        try:
            name = translator.translate(str(text), dest='en')
            name = name.text.replace(' ', '')
            url = 'http://cactus.nci.nih.gov/chemical/structure/' + name + '/smiles'
            ans = urlopen(url).read().decode('utf8')
            print(ans)
            size = (600, 250)
            m = Chem.MolFromSmiles(ans)
            fig = Draw.MolToImage(m, size=size)
            fig = fig.save('img.png')
            self.pixmap = QPixmap('img.png')
            self.label_2.setPixmap(self.pixmap)
        except:
            self.pixmap = QPixmap('error.png')
            self.label_2.setPixmap(self.pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
