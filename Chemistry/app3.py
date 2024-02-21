from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from window1 import Ui_MainMenu
from window2 import Ui_Window1
from window3 import Ui_Window2
from window4 import Ui_Window3

from chemlib import Compound
import mendeleev

app = QtWidgets.QApplication(sys.argv)

MainMenu = QtWidgets.QMainWindow()
main = Ui_MainMenu()
main.setupUi(MainMenu)
MainMenu.show()

def open_window1():
    global Window1
    Window1 = QtWidgets.QDialog()
    ui = Ui_Window1()
    ui.setupUi(Window1)
    MainMenu.close()
    Window1.show()

    def return_to_main():
        MainMenu.show()
        Window1.close()

    def result():
        try:
            compound = Compound(ui.lineEdit.text())
            result = QMessageBox()
            result.setWindowTitle('Результат')
            result.setText('Ответ: ' + '%.0f' % compound.molar_mass())
            result.setStandardButtons(QMessageBox.Ok)

            result.exec_()
        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setIcon(QMessageBox.Warning)
            error.setText('Неправильно введина формула')

            error.exec_()

    ui.pushButton.clicked.connect(return_to_main)
    ui.pushButton_2.clicked.connect(result)


def open_window2():
    global Window2
    Window2 = QtWidgets.QDialog()
    ui = Ui_Window2()
    ui.setupUi(Window2)
    MainMenu.close()
    Window2.show()

    def return_to_main():
        MainMenu.show()
        Window2.close()

    def result():
        try:
            compound = Compound(ui.lineEdit_2.text())
            atom = ui.lineEdit.text()
            result = QMessageBox()
            result.setWindowTitle('Результат')
            result.setText('Ответ: ' + '%.0f' % compound.percentage_by_mass(atom) + '%')
            result.setStandardButtons(QMessageBox.Ok)

            result.exec_()
        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setIcon(QMessageBox.Warning)
            error.setText('Неправильно введина формула')

            error.exec_()

    ui.pushButton.clicked.connect(return_to_main)
    ui.pushButton_2.clicked.connect(result)

    ui.pushButton.clicked.connect(return_to_main)


def open_window3():
    global Window3
    Window3 = QtWidgets.QDialog()
    ui = Ui_Window3()
    ui.setupUi(Window3)
    MainMenu.close()
    Window3.show()

    def return_to_main():
        MainMenu.show()
        Window3.close()

    def result():
        try:
            compound = Compound(ui.lineEdit_2.text())
            mass = int(ui.lineEdit_3.text())
            atom = mendeleev.element(ui.lineEdit.text())
            result = QMessageBox()
            result.setWindowTitle('Результат')
            result.setText('Ответ: ' + '%.0f' % (mass / (compound.percentage_by_mass(atom.symbol)/100)) + 'г.')
            result.setStandardButtons(QMessageBox.Ok)

            result.exec_()
        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setIcon(QMessageBox.Warning)
            error.setText('Неправильно введина формула')

            error.exec_()

    ui.pushButton.clicked.connect(return_to_main)
    ui.pushButton_2.clicked.connect(result)

    ui.pushButton.clicked.connect(return_to_main)


main.pushButton.clicked.connect(open_window1)
main.pushButton_2.clicked.connect(open_window2)
main.pushButton_3.clicked.connect(open_window3)

sys.exit(app.exec_())