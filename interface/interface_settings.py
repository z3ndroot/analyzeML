from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 398)
        MainWindow.setMinimumSize(QSize(463, 398))
        MainWindow.setMaximumSize(QSize(463, 398))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Light")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(21, 19, 72);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 80, 75, 23))
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI")
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 80, 231, 23))
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 80, 61, 23))
        font3 = QFont()
        font3.setFamily(u"Yu Gothic UI")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 120, 231, 23))
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 120, 75, 23))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 61, 23))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(110, 210, 231, 23))
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(350, 210, 75, 23))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 210, 61, 23))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(180, 300, 101, 31))
        font4 = QFont()
        font4.setFamily(u"Yu Gothic UI")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EvalAction", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dialog file", None))
        self.lineEdit_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rules file", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Save file", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
    # retranslateUi







