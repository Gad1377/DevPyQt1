"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil
from PySide6 import QtCore
import requests


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent(interval=0.1)
            ram_value = psutil.virtual_memory().percent
            self.systemInfoReceived.emit([cpu_value, ram_value])
            time.sleep(self.delay)


class WeatherHandler(QtCore.QThread):
    weatherDataReceived = QtCore.Signal(dict)
    errorOccurred = QtCore.Signal(str)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:
        self.__status = True

        while self.__status:
            try:
                response = requests.get(self.__api_url)
                data = response.json()
                self.weatherDataReceived.emit(data)

            except requests.RequestException as e:
                self.errorOccurred.emit(str(e))


            time.sleep(self.__delay)

    def stop(self) -> None:
        self.__status = False
