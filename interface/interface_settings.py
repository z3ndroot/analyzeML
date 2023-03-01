from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from interface import rc_logo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 450)
        MainWindow.setMinimumSize(QSize(460, 450))
        MainWindow.setMaximumSize(QSize(460, 450))
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
        self.pushButton.setGeometry(QRect(350, 160, 75, 23))
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
        self.lineEdit.setGeometry(QRect(110, 160, 231, 23))
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
        self.label.setGeometry(QRect(50, 160, 61, 23))
        font3 = QFont()
        font3.setFamily("Yu Gothic UI")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 290, 231, 23))
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
        self.pushButton_2.setGeometry(QRect(350, 290, 75, 23))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 10px;"
        )
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(50, 290, 61, 23))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(110, 330, 231, 23))
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
        self.pushButton_3.setGeometry(QRect(350, 330, 75, 23))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "border-radius: 10px;"
        )
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(50, 330, 61, 23))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setGeometry(QRect(180, 390, 101, 31))
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
        self.frame.setStyleSheet("border-image: url(:/ml/ml.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(60, 230, 101, 21))
        font5 = QFont()
        font5.setFamily("Nirmala UI")
        font5.setPointSize(10)
        self.comboBox.setFont(font5)
        self.comboBox.setStyleSheet(
            "#comboBox{\n"
            "	border: 2px solid rgb(46, 51, 73);\n"
            "	color: #FFF;\n"
            "	background-color: rgb(67, 75, 106);\n"
            "}\n"
            "\n"
            "#comboBox::drop-down{\n"
            "	border: 0px;\n"
            "}\n"
            "#comboBox::down-arrow{\n"
            "	image: url(:/ml/arrow.png);\n"
            "}\n"
            "\n"
            "\n"
            "#comboBox:on{\n"
            "	border: 2px solid rgb(80, 90, 127);\n"
            "}\n"
            "\n"
            "#comboBox QListView{\n"
            "	border: 1px solid rgb(80, 90, 127);\n"
            "	color: #FFF;\n"
            "}\n"
            "\n"
            "\n"
            ""
        )
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(80, 210, 71, 16))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(330, 210, 81, 16))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setGeometry(QRect(310, 230, 101, 21))
        self.comboBox_2.setFont(font5)
        self.comboBox_2.setStyleSheet(
            "#comboBox_2{\n"
            "	border: 2px solid rgb(46, 51, 73);\n"
            "	color: #FFF;\n"
            "	background-color: rgb(67, 75, 106);\n"
            "}\n"
            "\n"
            "#comboBox_2::drop-down{\n"
            "	border: 0px;\n"
            "}\n"
            "#comboBox_2::down-arrow{\n"
            "	image: url(:/ml/arrow.png);\n"
            "}\n"
            "\n"
            "\n"
            "#comboBox_2:on{\n"
            "	border: 2px solid rgb(80, 90, 127);\n"
            "}\n"
            "\n"
            "#comboBox_2 QListView{\n"
            "	border: 1px solid rgb(80, 90, 127);\n"
            "	color: #FFF;\n"
            "}\n"
            ""
        )
        self.MessageBox = QMessageBox()
        self.MessageBox.setIcon(QMessageBox.Information)
        self.MessageBox.setText("Done✅")
        self.MessageBox.setWindowTitle("Information")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MLAnalyze", None)
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
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "Name sheet", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "Name column", None)
        )
