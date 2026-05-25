"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущий основной монитор
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

import sys
from datetime import datetime
from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Проверка состояния окна")
        self.resize(650, 450)

        self.old_pos = self.pos()
        self.old_size = self.size()
        self.old_state = ""

        self.init_ui()
        self.init_signals()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.check_window_changes)
        self.timer.start(500)

    def init_ui(self) -> None:

        self.spinX = QtWidgets.QSpinBox()
        self.spinX.setRange(-2000, 2000)
        self.spinX.setValue(self.x())

        self.spinY = QtWidgets.QSpinBox()
        self.spinY.setRange(-2000, 2000)
        self.spinY.setValue(self.y())

        self.btnMove = QtWidgets.QPushButton("Переместить окно")
        self.btnInfo = QtWidgets.QPushButton("Получить параметры экрана")
        self.logEdit = QtWidgets.QPlainTextEdit()
        self.logEdit.setReadOnly(True)
        self.logEdit.setPlaceholderText("Здесь появятся параметры экрана...")

        layout_coords = QtWidgets.QHBoxLayout()
        layout_coords.addWidget(QtWidgets.QLabel("X:"))
        layout_coords.addWidget(self.spinX)
        layout_coords.addWidget(QtWidgets.QLabel("Y:"))
        layout_coords.addWidget(self.spinY)
        layout_coords.addWidget(self.btnMove)
        layout_coords.addStretch()


        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout_coords)
        layout_main.addWidget(self.btnInfo)
        layout_main.addWidget(self.logEdit)
        self.setLayout(layout_main)

    def init_signals(self) -> None:
        self.btnMove.clicked.connect(self.move_window)
        self.btnInfo.clicked.connect(self.show_screen_info)


    @staticmethod
    def get_time() -> str:
        return datetime.now().strftime("%H:%M:%S")


    def move_window(self) -> None:
        x = self.spinX.value()
        y = self.spinY.value()
        self.move(x, y)

        self.spinX.setValue(self.x())
        self.spinY.setValue(self.y())


    def show_screen_info(self) -> None:
        app = QtWidgets.QApplication.instance()
        screens = app.screens()
        primary_screen = app.primaryScreen()

        current_screen = app.screenAt(self.pos()) or primary_screen

        t = self.get_time()
        info_lines = [
            f"[{t}] Кол-во экранов: {len(screens)}",
            f"[{t}] Текущий основной монитор: {primary_screen.name()}",
            f"[{t}] Разрешение экрана: {primary_screen.geometry().width()}x{primary_screen.geometry().height()}",
            f"[{t}] На каком экране окно находится: {current_screen.name()}",
            f"[{t}] Размеры окна: {self.width()}x{self.height()}",
            f"[{t}] Минимальные размеры окна: {self.minimumWidth()}x{self.minimumHeight()}",
            f"[{t}] Текущее положение (координаты) окна: ({self.x()}, {self.y()})",
            f"[{t}] Координаты центра приложения: {self.geometry().center().x()}, {self.geometry().center().y()}",
            f"[{t}] Состояние окна: свернуто={self.isMinimized()}, развёрнуто={self.isMaximized()}, активно={self.isActiveWindow()}, отображено={self.isVisible()}"
            ]

        self.logEdit.appendPlainText("\n".join(info_lines))


    def check_window_changes(self) -> None:
        t = self.get_time()


        current_pos = self.pos()
        if current_pos != self.old_pos:
            print(
                f"[{t}] Перемещение окна: было ({self.old_pos.x()}, {self.old_pos.y()}) → стало ({current_pos.x()}, {current_pos.y()})")
            self.old_pos = current_pos


        current_size = self.size()
        if current_size != self.old_size:
            print(f"[{t}] Изменение размера окна: {current_size.width()}x{current_size.height()}")
            self.old_size = current_size


        current_state = f"min={self.isMinimized()} max={self.isMaximized()} active={self.isActiveWindow()} vis={self.isVisible()}"
        if current_state != self.old_state:
            print(
                f"[{t}] Состояние окна: свернуто={self.isMinimized()}, развёрнуто={self.isMaximized()}, активно={self.isActiveWindow()}, отображено={self.isVisible()}")
            self.old_state = current_state

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())

