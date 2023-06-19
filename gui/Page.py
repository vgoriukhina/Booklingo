# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Page.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_PageMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.AuthorNametextEdit = QTextEdit(self.centralwidget)
        self.AuthorNametextEdit.setReadOnly(True)
        self.AuthorNametextEdit.setObjectName(u"AuthorNametextEdit")
        self.AuthorNametextEdit.setGeometry(QRect(40, 0, 671, 31))
        self.AuthorNametextEdit.setStyleSheet(u" border: none;\n background-color: #f5e6c6;\n")

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 100, 651, 431))
        self.textEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none; background-color: #faf5ea;\n;  padding: 15px; ")
        self.textEdit.setFontPointSize(12)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(80, 560, 651, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.nextPageButton = QPushButton(self.frame_2)
        self.nextPageButton.setObjectName(u"nextPage")
        self.nextPageButton.setGeometry(QRect(610, 10, 41, 24))
        self.nextPageButton.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        icon1 = QIcon()
        iconThemeName = u"go-next"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../Python/Projects/venv/Lib/site-packages/PySide6", QSize(), QIcon.Normal, QIcon.Off)

        self.nextPageButton.setIcon(icon1)
        self.prevPageButton = QPushButton(self.frame_2)
        self.prevPageButton.setObjectName(u"previous page")
        self.prevPageButton.setGeometry(QRect(0, 10, 41, 24))
        self.prevPageButton.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        icon2 = QIcon()
        iconThemeName = u"go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"../Python/Projects/venv/Lib/site-packages/PySide6", QSize(), QIcon.Normal, QIcon.Off)

        self.prevPageButton.setIcon(icon2)
        self.PageslineEdit = QLineEdit(self.frame_2)
        self.PageslineEdit.setObjectName(u"PageslineEdit")
        self.PageslineEdit.setGeometry(QRect(250, 10, 113, 21))
        self.PageslineEdit.setStyleSheet(u" border: none;\n"
"    box-shadow: none; background-color: #faf5ea;\n")
        self.questionsButton = QPushButton(self.centralwidget)
        self.questionsButton.setObjectName(u"pushButton_3")
        self.questionsButton.setGeometry(QRect(280, 530, 181, 24))
        #self.questionsButton.set
        self.questionsButton.setStyleSheet(u" border: none;\n"
"    box-shadow: none;")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reading", None))
        self.AuthorNametextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        """
        self.KontoButton_3.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.MyBooksButton_3.setText(QCoreApplication.translate("MainWindow", u"MyBooks", None))
        self.FindButton_3.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.FavoriteButton_3.setText(QCoreApplication.translate("MainWindow", u"Fav", None))
        self.ExitButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.HelpButton_3.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        """
        self.nextPageButton.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.prevPageButton.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.PageslineEdit.setText(QCoreApplication.translate("MainWindow", u"page/page", None))
        self.questionsButton.setText(QCoreApplication.translate("MainWindow", u"Check understanding", None))
    # retranslateUi
