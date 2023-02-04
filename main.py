from interface import MyApp

from PySide2 import QtWidgets
from sys import argv



def main():
    app = QtWidgets.QApplication(argv)
    window = MyApp()
    window.show()
    app.exec_()




if __name__ == '__main__':
    main()
