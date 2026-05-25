"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets,  QtCore
from b_systeminfo_widget import SystemMonitorWidget
from c_weatherapi_widget import WeatherWidget


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Лабораторный практикум")
        self.resize(1000, 700)

        self.init_ui()

    def init_ui(self) -> None:
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)

        self.system_monitor = SystemMonitorWidget()
        splitter.addWidget(self.system_monitor)

        self.weather_widget = WeatherWidget()
        splitter.addWidget(self.weather_widget)

        splitter.setSizes([400, 400])

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(splitter)
        central_widget.setLayout(layout)

        self.statusBar().showMessage("Оба виджета работают одновременно")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName("StudentOrg")
    app.setApplicationName("LaboratoryApp")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())