from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QLabel
)

from gui.configuration_tab import ConfigurationTab
from gui.analysis_tab import AnalysisTab

import sys


class AnimationTab(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel("Animation Tab")
        )

        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Electromagnetic Accelerator Simulator"
        )

        self.resize(
            1400,
            900
        )

        self.setup_ui()

    def setup_ui(self):

        self.tabs = QTabWidget()

        self.configuration_tab = ConfigurationTab()

        self.analysis_tab = AnalysisTab()

        self.animation_tab = AnimationTab()

        self.configuration_tab.analysis_tab = (
            self.analysis_tab
        )

        self.tabs.addTab(
            self.configuration_tab,
            "Configuration"
        )

        self.tabs.addTab(
            self.analysis_tab,
            "Analysis"
        )

        self.tabs.addTab(
            self.animation_tab,
            "Animation"
        )

        self.setCentralWidget(
            self.tabs
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())