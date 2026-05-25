import sys
import os
import time
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QProgressBar, QPlainTextEdit, QLabel,
    QFileDialog, QMessageBox, QSizePolicy
)
from PySide6.QtCore import QObject, Signal, Slot, QThread, Qt


def format_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.2f} {units[i]}"


class ScannerWorker(QObject):

    progress_changed = Signal(int, int)
    scan_finished = Signal(int, int)
    error_occurred = Signal(str)

    @Slot(str)
    def run_scan(self, folder_path: str):
        try:
            file_list = []
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_list.append(os.path.join(root, file))

            total_files = len(file_list)
            total_size = 0

            if total_files == 0:
                self.scan_finished.emit(0, 0)
                return

            for i, fpath in enumerate(file_list):
                try:
                    total_size += os.path.getsize(fpath)
                except OSError:
                    pass

                if i % 50 == 0 or i == total_files - 1:
                    self.progress_changed.emit(i + 1, total_files)

            self.scan_finished.emit(total_files, total_size)

        except Exception as e:
            self.error_occurred.emit(str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сканер папки")
        self.resize(650, 450)

        self.thread = None
        self.worker = None
        self.is_scanning = False

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)

        path_layout = QHBoxLayout()
        self.line_path = QLineEdit()
        self.line_path.setPlaceholderText("Путь к папке...")
        self.line_path.setReadOnly(True)
        self.btn_select = QPushButton("Выбрать папку")
        path_layout.addWidget(self.line_path)
        path_layout.addWidget(self.btn_select)
        main_layout.addLayout(path_layout)

        control_layout = QHBoxLayout()
        self.btn_start = QPushButton("Начать сканирование")
        self.btn_start.setMinimumWidth(150)
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(True)
        control_layout.addWidget(self.btn_start)
        control_layout.addWidget(self.progress_bar, stretch=1)
        main_layout.addLayout(control_layout)

        self.label_stats = QLabel("Готов к работе")
        self.label_stats.setAlignment(Qt.AlignCenter)
        self.label_stats.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
        main_layout.addWidget(self.label_stats)

        main_layout.addWidget(QLabel("Лог операций:"), alignment=Qt.AlignLeft)
        self.log_text = QPlainTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setStyleSheet("background-color: #f5f5f5; font-family: monospace;")
        main_layout.addWidget(self.log_text)

        self.btn_select.clicked.connect(self.select_folder)
        self.btn_start.clicked.connect(self.start_scan)

    def log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.appendPlainText(f"[{timestamp}] {message}")
        self.log_text.verticalScrollBar().setValue(self.log_text.verticalScrollBar().maximum())

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder:
            self.line_path.setText(folder)
            self.log(f"Выбрана папка: {folder}")

    def start_scan(self):
        folder_path = self.line_path.text().strip()

        if self.is_scanning:
            QMessageBox.warning(self, "Внимание", "Сканирование уже выполняется!")
            return
        if not folder_path or not os.path.isdir(folder_path):
            QMessageBox.critical(self, "Ошибка", "Укажите верную  папку.")
            return

        self.is_scanning = True
        self.btn_start.setEnabled(False)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(100)
        self.label_stats.setText("Сканирование...")
        self.log("Начало сканирования...")

        self.thread = QThread()
        self.worker = ScannerWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(lambda: self.worker.run_scan(folder_path))
        self.worker.progress_changed.connect(self.update_progress)
        self.worker.scan_finished.connect(self.finish_scan)
        self.worker.error_occurred.connect(self.handle_error)

        self.worker.scan_finished.connect(self.thread.quit)
        self.worker.scan_finished.connect(self.worker.deleteLater)
        self.worker.error_occurred.connect(self.thread.quit)
        self.worker.error_occurred.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    @Slot(int, int)
    def update_progress(self, current: int, total: int):
        if total > 0:
            self.progress_bar.setMaximum(total)
            self.progress_bar.setValue(current)
            self.label_stats.setText(f"Обработано: {current} из {total} файлов")

    @Slot(int, int)
    def finish_scan(self, file_count: int, total_size_bytes: int):
        self.is_scanning = False
        self.btn_start.setEnabled(True)
        self.progress_bar.setValue(self.progress_bar.maximum())

        size_str = format_size(total_size_bytes)
        self.label_stats.setText(f"Найдено файлов: {file_count} | Общий размер: {size_str}")

        self.log(f"Сканирование завершено.")
        self.log(f"Путь: {self.line_path.text()}")
        self.log(f"Файлов: {file_count}, Размер: {size_str}")

    @Slot(str)
    def handle_error(self, message: str):
        self.is_scanning = False
        self.btn_start.setEnabled(True)
        self.label_stats.setText("Ошибка при сканировании")
        self.log(f"ОШИБКА: {message}")
        QMessageBox.critical(self, "Ошибка сканирования", message)

    def closeEvent(self, event):
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait(2000)
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())