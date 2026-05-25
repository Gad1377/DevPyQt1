# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 380)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.row1 = QHBoxLayout()
        self.row1.setObjectName(u"row1")
        self.labelFirst = QLabel(Form)
        self.labelFirst.setObjectName(u"labelFirst")

        self.row1.addWidget(self.labelFirst)

        self.sliderFirst = QSlider(Form)
        self.sliderFirst.setObjectName(u"sliderFirst")
        self.sliderFirst.setOrientation(Qt.Orientation.Horizontal)

        self.row1.addWidget(self.sliderFirst)

        self.lineEditFirst = QLineEdit(Form)
        self.lineEditFirst.setObjectName(u"lineEditFirst")

        self.row1.addWidget(self.lineEditFirst)


        self.verticalLayout.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.setObjectName(u"row2")
        self.labelSecond = QLabel(Form)
        self.labelSecond.setObjectName(u"labelSecond")

        self.row2.addWidget(self.labelSecond)

        self.sliderSecond = QSlider(Form)
        self.sliderSecond.setObjectName(u"sliderSecond")
        self.sliderSecond.setOrientation(Qt.Orientation.Horizontal)

        self.row2.addWidget(self.sliderSecond)

        self.lineEditSecond = QLineEdit(Form)
        self.lineEditSecond.setObjectName(u"lineEditSecond")

        self.row2.addWidget(self.lineEditSecond)


        self.verticalLayout.addLayout(self.row2)

        self.spacerButtons = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacerButtons)

        self.buttonsRow = QHBoxLayout()
        self.buttonsRow.setSpacing(10)
        self.buttonsRow.setObjectName(u"buttonsRow")
        self.btnPlus = QPushButton(Form)
        self.btnPlus.setObjectName(u"btnPlus")

        self.buttonsRow.addWidget(self.btnPlus)

        self.btnMinus = QPushButton(Form)
        self.btnMinus.setObjectName(u"btnMinus")

        self.buttonsRow.addWidget(self.btnMinus)

        self.btnMult = QPushButton(Form)
        self.btnMult.setObjectName(u"btnMult")

        self.buttonsRow.addWidget(self.btnMult)

        self.btnDiv = QPushButton(Form)
        self.btnDiv.setObjectName(u"btnDiv")

        self.buttonsRow.addWidget(self.btnDiv)


        self.verticalLayout.addLayout(self.buttonsRow)

        self.spacerResult = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacerResult)

        self.labelResult = QLabel(Form)
        self.labelResult.setObjectName(u"labelResult")
        self.labelResult.setStyleSheet(u"color: green; font-size: 48px; font-weight: bold;")
        self.labelResult.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelResult, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.labelFirst.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e:", None))
        self.lineEditFirst.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.labelSecond.setText(QCoreApplication.translate("Form", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e:", None))
        self.lineEditSecond.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.btnPlus.setText(QCoreApplication.translate("Form", u"+", None))
        self.btnMinus.setText(QCoreApplication.translate("Form", u"-", None))
        self.btnMult.setText(QCoreApplication.translate("Form", u"*", None))
        self.btnDiv.setText(QCoreApplication.translate("Form", u"/", None))
        self.labelResult.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())