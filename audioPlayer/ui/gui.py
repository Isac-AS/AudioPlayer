import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

class AudioPlayerUi():
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()

    def start(self):
        self.main_window.show()
        self.app.exec()
