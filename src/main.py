from gui.main_window import MainWindow
from gui.configuration_tab import ConfigurationTab
from PySide6.QtWidgets import QApplication

import sys


app = QApplication(sys.argv)

window = MainWindow()

window.show()

sys.exit(app.exec())