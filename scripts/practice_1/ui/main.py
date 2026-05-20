import sys
from PySide6.QtWidgets import QApplication, QWidget
from login import Ui_Form


class LoginWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_login_click)

    def on_login_click(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(f"Попытка входа: {username}, пароль: {password}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())