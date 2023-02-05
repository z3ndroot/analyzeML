from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from interface import logo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 398)
        MainWindow.setMinimumSize(QSize(463, 398))
        MainWindow.setMaximumSize(QSize(463, 398))
        font = QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(46, 51, 73);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(350, 180, 75, 23))
        font1 = QFont()
        font1.setFamily("Yu Gothic UI")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 10px;"
        )
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(110, 180, 231, 23))
        font2 = QFont()
        font2.setFamily("Nirmala UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(
            "	border: 2px solid rgb(46, 51, 73);\n"
            "	border-radius: 20px;\n"
            "	color: #FFF;\n"
            "	\n"
            "background-color: rgb(67, 75, 106);\n"
            "\n"
            "\n"
            ""
        )
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(50, 180, 61, 23))
        font3 = QFont()
        font3.setFamily("Yu Gothic UI")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 220, 231, 23))
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(
            "	border: 2px solid rgb(46, 51, 73);\n"
            "	border-radius: 20px;\n"
            "	color: #FFF;\n"
            "	\n"
            "background-color: rgb(67, 75, 106);"
        )
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 220, 75, 23))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 10px;"
        )
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(50, 220, 61, 23))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(110, 280, 231, 23))
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setStyleSheet(
            "	border: 2px solid rgb(46, 51, 73);\n"
            "	border-radius: 20px;\n"
            "	color: #FFF;\n"
            "	\n"
            "background-color: rgb(67, 75, 106);"
        )
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QRect(350, 280, 75, 23))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 10px;"
        )
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(50, 280, 61, 23))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setGeometry(QRect(180, 330, 101, 31))
        font4 = QFont()
        font4.setFamily("Yu Gothic UI")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setWeight(50)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(
            "background-color: rgb(101, 111, 170);\n"
            "border-radius: 10px;\n"
            "color: rgb(255, 255, 255);"
        )
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(190, 40, 91, 91))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/ml.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Browse", None)
        )
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Dialog file", None)
        )
        self.lineEdit_2.setText("")
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Browse", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "Rules file", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "Browse", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Save file", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", "Analyze", None)
        )
