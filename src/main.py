print("program started")

from gui.main_window import MainWindow

print("imported main window")

from PySide6.QtWidgets import QApplication

print("imported QApplication")

import sys

app = QApplication(sys.argv)

print("app created")

window = MainWindow()

print("window created")

window.show()

print("window shown")

sys.exit(app.exec())