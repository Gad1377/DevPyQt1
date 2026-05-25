"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from a_threads import SystemInfo
from PySide6 import QtWidgets, QtCore


class SystemMonitorWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Монитор системы")
        self.resize(300, 150)

        self.init_ui()
        self.init_signals()


        self.system_thread = SystemInfo()
        self.system_thread.systemInfoReceived.connect(self.update_info)
        self.system_thread.start()

    def init_ui(self) -> None:

        self.spin_delay = QtWidgets.QSpinBox()
        self.spin_delay.setRange(1, 60)
        self.spin_delay.setValue(1)
        self.spin_delay.setSuffix(" сек")


        self.label_cpu = QtWidgets.QLabel("Загрузка CPU: -- %")
        self.label_ram = QtWidgets.QLabel("Загрузка RAM: -- %")


        self.label_cpu.setStyleSheet("font-weight: bold;")
        self.label_ram.setStyleSheet("font-weight: bold;")


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Интервал обновления:"))
        layout.addWidget(self.spin_delay)
        layout.addSpacing(10)
        layout.addWidget(self.label_cpu)
        layout.addWidget(self.label_ram)
        layout.addStretch()

        self.setLayout(layout)

    def init_signals(self) -> None:

        self.spin_delay.valueChanged.connect(self.on_delay_changed)

    def on_delay_changed(self, value: int) -> None:

        self.system_thread.delay = value
        print(f"[UI] Задержка изменена на: {value} сек")

    def update_info(self, data: list) -> None:

        cpu, ram = data
        self.label_cpu.setText(f"Загрузка CPU: {cpu:.1f} %")
        self.label_ram.setText(f"Загрузка RAM: {ram:.1f} %")

    def closeEvent(self, event) -> None:

        if self.system_thread.isRunning():
            self.system_thread.terminate()  # для учебного примера допустимо
            self.system_thread.wait()
        super().closeEvent(event)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = SystemMonitorWidget()
    window.show()

    sys.exit(app.exec())