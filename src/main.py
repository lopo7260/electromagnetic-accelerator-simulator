print("1")

from gui.main_window import MainWindow

print("2")

from PySide6.QtWidgets import QApplication

print("3")

import sys

app = QApplication(sys.argv)

print("4")

window = MainWindow()

print("5")

window.show()

print("6")

sys.exit(app.exec())