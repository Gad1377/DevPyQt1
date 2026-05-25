# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'd_engine.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(558, 297)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout1 = QVBoxLayout()
        self.layout1.setObjectName(u"layout1")
        self.slider1 = QSlider(self.groupBox)
        self.slider1.setObjectName(u"slider1")
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(100)
        self.slider1.setOrientation(Qt.Orientation.Vertical)
        self.slider1.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.layout1.addWidget(self.slider1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout1.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.layout1)

        self.layout2 = QVBoxLayout()
        self.layout2.setObjectName(u"layout2")
        self.slider2 = QSlider(self.groupBox)
        self.slider2.setObjectName(u"slider2")
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(100)
        self.slider2.setOrientation(Qt.Orientation.Vertical)
        self.slider2.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.layout2.addWidget(self.slider2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout2.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.layout2)

        self.layout3 = QVBoxLayout()
        self.layout3.setObjectName(u"layout3")
        self.slider3 = QSlider(self.groupBox)
        self.slider3.setObjectName(u"slider3")
        self.slider3.setMinimum(0)
        self.slider3.setMaximum(100)
        self.slider3.setOrientation(Qt.Orientation.Vertical)
        self.slider3.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.layout3.addWidget(self.slider3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout3.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.layout3)

        self.layout4 = QVBoxLayout()
        self.layout4.setObjectName(u"layout4")
        self.slider4 = QSlider(self.groupBox)
        self.slider4.setObjectName(u"slider4")
        self.slider4.setMinimum(0)
        self.slider4.setMaximum(100)
        self.slider4.setOrientation(Qt.Orientation.Vertical)
        self.slider4.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.layout4.addWidget(self.slider4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label4 = QLabel(self.groupBox)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout4.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.layout4)

        self.layout5 = QVBoxLayout()
        self.layout5.setObjectName(u"layout5")
        self.sliderH = QSlider(self.groupBox)
        self.sliderH.setObjectName(u"sliderH")
        self.sliderH.setMinimum(0)
        self.sliderH.setMaximum(100)
        self.sliderH.setOrientation(Qt.Orientation.Horizontal)

        self.layout5.addWidget(self.sliderH)

        self.label5 = QLabel(self.groupBox)
        self.label5.setObjectName(u"label5")

        self.layout5.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.layout5)

        self.layout6 = QVBoxLayout()
        self.layout6.setObjectName(u"layout6")
        self.sliderTotal = QSlider(self.groupBox)
        self.sliderTotal.setObjectName(u"sliderTotal")
        self.sliderTotal.setMinimum(0)
        self.sliderTotal.setMaximum(100)
        self.sliderTotal.setOrientation(Qt.Orientation.Vertical)
        self.sliderTotal.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.layout6.addWidget(self.sliderTotal, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelTotal = QLabel(self.groupBox)
        self.labelTotal.setObjectName(u"labelTotal")
        self.labelTotal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout6.addWidget(self.labelTotal)


        self.horizontalLayout.addLayout(self.layout6)


        self.verticalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label5.setText("")
        self.labelTotal.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())