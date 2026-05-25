# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'f_book.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 450)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelBookTitle = QLabel(Form)
        self.labelBookTitle.setObjectName(u"labelBookTitle")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelBookTitle.setFont(font)
        self.labelBookTitle.setStyleSheet(u"color: red;")

        self.verticalLayout.addWidget(self.labelBookTitle)

        self.plainTextEditBooks = QPlainTextEdit(Form)
        self.plainTextEditBooks.setObjectName(u"plainTextEditBooks")
        self.plainTextEditBooks.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEditBooks)

        self.labelPaymentTitle = QLabel(Form)
        self.labelPaymentTitle.setObjectName(u"labelPaymentTitle")
        self.labelPaymentTitle.setFont(font)
        self.labelPaymentTitle.setStyleSheet(u"color: red;")

        self.verticalLayout.addWidget(self.labelPaymentTitle)

        self.radioCard = QRadioButton(Form)
        self.radioCard.setObjectName(u"radioCard")

        self.verticalLayout.addWidget(self.radioCard)

        self.radioQR = QRadioButton(Form)
        self.radioQR.setObjectName(u"radioQR")

        self.verticalLayout.addWidget(self.radioQR)

        self.radioCash = QRadioButton(Form)
        self.radioCash.setObjectName(u"radioCash")

        self.verticalLayout.addWidget(self.radioCash)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonPay = QPushButton(Form)
        self.buttonPay.setObjectName(u"buttonPay")

        self.verticalLayout.addWidget(self.buttonPay)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041e\u043f\u043b\u0430\u0442\u0430", None))
        self.labelBookTitle.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043d\u0438\u0433\u0443", None))
        self.plainTextEditBooks.setPlainText(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440 \u0438 \u0443\u0437\u043d\u0438\u043a \u0410\u0437\u043a\u0430\u0431\u0430\u043d\u0430 \u0414\u0436\u043e\u0430\u043d \u0420\u043e\u0443\u043b\u0438\u043d\u0433\n"
"\u0411\u043b\u0430\u0433\u043e\u0441\u043b\u043e\u0432\u0435\u043d\u0438\u0435 \u043d\u0435\u0431\u043e\u0436\u0438\u0442\u0435\u043b\u0435\u0439. \u0422\u043e\u043c 3 \u041c\u043e\u0441\u044f\u043d \u0422\u0443\u043d\u0441\u044e\n"
"\u0423\u043d\u0435\u0441\u0435\u043d\u043d\u044b\u0435 \u0432\u0435\u0442\u0440\u043e\u043c \u041c\u0430\u0440\u0433\u0430\u0440\u0435\u0442 \u041c\u0438\u0442\u0447\u0435\u043b\u043b", None))
        self.labelPaymentTitle.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.radioCard.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u043a\u0430\u0440\u0442\u0435", None))
        self.radioQR.setText(QCoreApplication.translate("Form", u"\u041f\u043e QR", None))
        self.radioCash.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
        self.buttonPay.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())