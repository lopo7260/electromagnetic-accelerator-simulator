from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QComboBox,
    QLabel
)
from graphics.plot import (
    plot_trajectory_3d,
    plot_trajectory_projections,
    plot_final_beam_scatter
)

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg
)

from matplotlib.figure import Figure


class AnalysisTab(QWidget):

    def __init__(self):
        super().__init__()

        self.history = None

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel("Plot Type")
        )

        self.plot_selector = QComboBox()

        self.plot_selector.addItems([
            "Trajectory 3D",
            "Trajectory Projections",
            "Final Beam Scatter"

        ])

        layout.addWidget(
            self.plot_selector
        )
        self.refresh_button = QPushButton(
            "Refresh"
        )

        layout.addWidget(
            self.refresh_button
        )

        self.setLayout(layout)

        self.refresh_button.clicked.connect(
            self.refresh_plot
        )

        self.figure = Figure()

        self.canvas = FigureCanvasQTAgg(
            self.figure
        )

        layout.addWidget(
            self.canvas
        )



    def set_history(self, history):

        self.history = history
#         print("History set in AnalysisTab")
            
    def refresh_plot(self):

        if self.history is None:
            return

        trajectories = (
            self.history.get_trajectories()
        )
        
        plot_type = (
    self.plot_selector.currentText()
)

        if plot_type == "Trajectory 3D":
            plot_trajectory_3d(
                self.figure,
                trajectories
            )
        elif plot_type == "Trajectory Projections":
            plot_trajectory_projections(
                self.figure,
                trajectories
            )
        elif plot_type == "Final Beam Scatter":
            plot_final_beam_scatter(
                self.figure,
                trajectories
            )

        self.canvas.draw()