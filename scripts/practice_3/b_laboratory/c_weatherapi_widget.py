"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
from a_threads import WeatherHandler
from PySide6 import QtWidgets, QtCore


class WeatherWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Погода по координатам")
        self.resize(400, 350)

        self.thread_running = False
        self.weather_thread = None
        self.spin_lat = None
        self.spin_lon = None
        self.spin_delay = None
        self.btn_toggle = None
        self.text_weather = None

        self.init_ui()
        self.init_signals()

    def init_ui(self) -> None:
        self.spin_lat = QtWidgets.QDoubleSpinBox()
        self.spin_lat.setRange(-90, 90)
        self.spin_lat.setValue(59.93)
        self.spin_lat.setDecimals(4)
        self.spin_lat.setSingleStep(0.01)

        self.spin_lon = QtWidgets.QDoubleSpinBox()
        self.spin_lon.setRange(-180, 180)
        self.spin_lon.setValue(30.33)
        self.spin_lon.setDecimals(4)
        self.spin_lon.setSingleStep(0.01)

        layout_coords = QtWidgets.QHBoxLayout()
        layout_coords.addWidget(QtWidgets.QLabel("Широта:"))
        layout_coords.addWidget(self.spin_lat)
        layout_coords.addWidget(QtWidgets.QLabel("Долгота:"))
        layout_coords.addWidget(self.spin_lon)

        self.spin_delay = QtWidgets.QSpinBox()
        self.spin_delay.setRange(5, 300)
        self.spin_delay.setValue(10)
        self.spin_delay.setSuffix(" сек")

        layout_delay = QtWidgets.QHBoxLayout()
        layout_delay.addWidget(QtWidgets.QLabel("Интервал обновления:"))
        layout_delay.addWidget(self.spin_delay)
        layout_delay.addStretch()

        self.btn_toggle = QtWidgets.QPushButton("▶ Запустить")
        self.btn_toggle.setCheckable(True)
        self.btn_toggle.setStyleSheet("""
            QPushButton:checked { background-color: #ffcccc; }
        """)

        self.text_weather = QtWidgets.QPlainTextEdit()
        self.text_weather.setReadOnly(True)
        self.text_weather.setPlaceholderText("Здесь появится информация о погоде...")
        self.text_weather.setMinimumHeight(150)

        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout_coords)
        layout_main.addLayout(layout_delay)
        layout_main.addWidget(self.btn_toggle)
        layout_main.addWidget(self.text_weather)
        self.setLayout(layout_main)

    def init_signals(self) -> None:
        self.btn_toggle.toggled.connect(self.on_toggle_thread)

    def on_toggle_thread(self, checked: bool) -> None:
        if checked:
            lat = self.spin_lat.value()
            lon = self.spin_lon.value()
            delay = self.spin_delay.value()

            self.weather_thread = WeatherHandler(lat, lon)
            self.weather_thread.setDelay(delay)
            self.weather_thread.weatherDataReceived.connect(self.on_weather_received)
            self.weather_thread.errorOccurred.connect(self.on_weather_error)
            self.weather_thread.start()

            self.spin_lat.setEnabled(False)
            self.spin_lon.setEnabled(False)
            self.spin_delay.setEnabled(False)

            self.btn_toggle.setText("■ Остановить")
            self.text_weather.appendPlainText(f"[{self.get_time()}] Запрос погоды запущен...")
            self.thread_running = True

        else:
            if hasattr(self, 'weather_thread') and self.weather_thread.isRunning():
                self.weather_thread.stop()
                self.weather_thread.wait()


            self.spin_lat.setEnabled(True)
            self.spin_lon.setEnabled(True)
            self.spin_delay.setEnabled(True)


            self.btn_toggle.setText("▶ Запустить")
            self.text_weather.appendPlainText(f"[{self.get_time()}] Запрос погоды остановлен")
            self.thread_running = False

    def on_weather_received(self, data: dict) -> None:
        try:

            current = data.get("current_weather", {})
            temp = current.get("temperature", "N/A")
            windspeed = current.get("windspeed", "N/A")
            weather_code = current.get("weathercode", "N/A")
            time_update = current.get("time", "N/A")


            weather_text = (
                f"⏰ Время обновления: {time_update}\n"
                f"🌡️ Температура: {temp} °C\n"
                f"💨 Ветер: {windspeed} км/ч\n"
                f"🔢 Код погоды: {weather_code}\n"
                f"{'─' * 30}"
            )

            self.text_weather.insertPlainText(weather_text + "\n")
            self.text_weather.verticalScrollBar().setValue(
                self.text_weather.verticalScrollBar().maximum()
            )
        except Exception as e:
            self.text_weather.appendPlainText(f"[Ошибка парсинга] {e}")

    def on_weather_error(self, error_msg: str) -> None:

        self.text_weather.appendPlainText(f"[❌ Ошибка] {error_msg}")

    @staticmethod
    def get_time() -> str:

        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")

    def closeEvent(self, event) -> None:

        if self.thread_running and hasattr(self, 'weather_thread'):
            self.weather_thread.stop()
            self.weather_thread.wait()
        super().closeEvent(event)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = WeatherWidget()
    window.show()

    sys.exit(app.exec())
