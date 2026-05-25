# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'e_profile.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 200)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.labelSurname = QLabel(Form)
        self.labelSurname.setObjectName(u"labelSurname")

        self.hboxLayout.addWidget(self.labelSurname)

        self.lineEditSurname = QLineEdit(Form)
        self.lineEditSurname.setObjectName(u"lineEditSurname")

        self.hboxLayout.addWidget(self.lineEditSurname)


        self.verticalLayout.addLayout(self.hboxLayout)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.labelName = QLabel(Form)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setMinimumSize(QSize(100, 0))

        self.hboxLayout1.addWidget(self.labelName)

        self.lineEditName = QLineEdit(Form)
        self.lineEditName.setObjectName(u"lineEditName")

        self.hboxLayout1.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.hboxLayout1)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.labelPatronymic = QLabel(Form)
        self.labelPatronymic.setObjectName(u"labelPatronymic")

        self.hboxLayout2.addWidget(self.labelPatronymic)

        self.lineEditPatronymic = QLineEdit(Form)
        self.lineEditPatronymic.setObjectName(u"lineEditPatronymic")

        self.hboxLayout2.addWidget(self.lineEditPatronymic)


        self.verticalLayout.addLayout(self.hboxLayout2)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.labelPhone = QLabel(Form)
        self.labelPhone.setObjectName(u"labelPhone")

        self.hboxLayout3.addWidget(self.labelPhone)

        self.lineEditPhone = QLineEdit(Form)
        self.lineEditPhone.setObjectName(u"lineEditPhone")

        self.hboxLayout3.addWidget(self.lineEditPhone)


        self.verticalLayout.addLayout(self.hboxLayout3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.labelSurname.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEditSurname.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.labelName.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.lineEditName.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.labelPatronymic.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEditPatronymic.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.labelPhone.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEditPhone.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())