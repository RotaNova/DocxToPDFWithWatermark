# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKZzsXq.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 781, 531))
        self.layout = QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setObjectName(u"layout")
        self.layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.Title = QLabel(self.verticalLayoutWidget)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setPointSize(24)
        self.Title.setFont(font)
        self.Title.setAcceptDrops(False)
        self.Title.setLayoutDirection(Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setScaledContents(False)
        self.Title.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.Title)

        self.Discription = QLabel(self.verticalLayoutWidget)
        self.Discription.setObjectName(u"Discription")
        self.Discription.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.Discription)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pickWorkPath = QPushButton(self.verticalLayoutWidget)
        self.pickWorkPath.setObjectName(u"pickWorkPath")

        self.horizontalLayout.addWidget(self.pickWorkPath)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.workPath = QLabel(self.verticalLayoutWidget)
        self.workPath.setObjectName(u"workPath")

        self.horizontalLayout.addWidget(self.workPath)


        self.layout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chooseWaterMarkFile = QPushButton(self.verticalLayoutWidget)
        self.chooseWaterMarkFile.setObjectName(u"chooseWaterMarkFile")

        self.horizontalLayout_2.addWidget(self.chooseWaterMarkFile)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.watermarkFile = QLabel(self.verticalLayoutWidget)
        self.watermarkFile.setObjectName(u"watermarkFile")

        self.horizontalLayout_2.addWidget(self.watermarkFile)


        self.layout.addLayout(self.horizontalLayout_2)

        self.results = QPlainTextEdit(self.verticalLayoutWidget)
        self.results.setObjectName(u"results")
        self.results.setReadOnly(True)

        self.layout.addWidget(self.results)

        self.startConvert = QPushButton(self.verticalLayoutWidget)
        self.startConvert.setObjectName(u"startConvert")
        self.startConvert.setEnabled(False)

        self.layout.addWidget(self.startConvert)

        self.authorLabel = QLabel(self.verticalLayoutWidget)
        self.authorLabel.setObjectName(u"authorLabel")
        self.authorLabel.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.authorLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Word\u6587\u4ef6\u6279\u91cf\u8f6cPDF\uff0c \u6279\u91cf\u6dfb\u52a0\u6c34\u5370", None))
        self.Discription.setText(QCoreApplication.translate("MainWindow", u"\u8bf4\u660e\uff1a\u8f6c\u6362\u5b8c\u7684PDF\u6587\u4ef6\u4fdd\u5b58\u5728\u8f6f\u4ef6\u6267\u884c\u7684\u5f53\u524d\u8def\u5f84\u7684PDF\u76ee\u5f55\u4e0b\uff0c\u6dfb\u52a0\u4e86\u6c34\u5370\u7684PDF\u6587\u4ef6\u4fdd\u5b58\u5728\u76f8\u540c\u8def\u5f84\u7684PDFMarked\u76ee\u5f55\u4e0b\u3002", None))
        self.pickWorkPath.setText(QCoreApplication.translate("MainWindow", u"\u9009\u53d6\u6587\u4ef6\u76ee\u5f55", None))
        self.workPath.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u53d6\u8981\u8fdb\u884c\u6279\u91cfPDF\u8f6c\u6362\u7684Word\u6587\u6863\u7684\u76ee\u5f55", None))
        self.chooseWaterMarkFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u53d6\u6c34\u5370\u6587\u4ef6", None))
        self.watermarkFile.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u53d6\u8981\u6dfb\u52a0\u7684\u6c34\u5370\u6a21\u677f\u6587\u4ef6\uff0c\u683c\u5f0f\u4e3aPDF", None))
        self.startConvert.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.authorLabel.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u7248\u672c:v0.3 \u65e5\u671f\uff1a2022\u5e745\u67089\u65e5 \u7248\u6743@QILIN YOU", None))
    # retranslateUi

