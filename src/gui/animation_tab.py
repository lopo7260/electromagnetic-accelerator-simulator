from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSpinBox
)

from PySide6.QtCore import QTimer

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg
)

from matplotlib.figure import Figure
import numpy as np


class AnimationTab(QWidget):

    def __init__(self):
        super().__init__()

        self.history = None

        self.current_frame = 0

        self.timer = QTimer()
        self.timer.timeout.connect(
            self.update_frame
        )

        self.scatter = None

        self.trajectories = None

        self.selected_indices = None

        self.max_animation_frames = 200

        self.displayed_frames = None

        self.simulation_dt = 0.01

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        self.particle_selector = QSpinBox()

        self.particle_selector.setMinimum(1)

        self.play_button = QPushButton(
            "Play"
        )

        self.pause_button = QPushButton(
            "Pause"
        )

        self.reset_button = QPushButton(
            "Reset"
        )
        self.time_label = QLabel(
            "Simulated time: 0.0 s"
        )

        layout.addWidget(
            self.time_label
        )

        controls = QHBoxLayout()

        controls.addWidget(
            QLabel("Particles displayed:")
        )

        controls.addWidget(
            self.particle_selector
        )

        controls.addWidget(
            self.play_button
        )

        controls.addWidget(
            self.pause_button
        )

        controls.addWidget(
            self.reset_button
        )

        layout.addLayout(
            controls
        )
        self.figure = Figure()

        self.canvas = FigureCanvasQTAgg(
            self.figure
        )

        layout.addWidget(
            self.canvas
        )
        self.play_button.clicked.connect(
            self.play_animation
        )

        self.pause_button.clicked.connect(
            self.pause_animation
        )

        self.reset_button.clicked.connect(
            self.reset_animation
        )

        self.particle_selector.valueChanged.connect(
            self.redraw_current_frame
        )

        self.setLayout(layout)



    def set_history(self, history):

        self.history = history

        trajectories = (
            history.get_trajectories()
        )

        self.x_min = trajectories[:, :, 0].min()
        self.x_max = trajectories[:, :, 0].max()

        self.y_min = trajectories[:, :, 1].min()
        self.y_max = trajectories[:, :, 1].max()

        self.z_min = trajectories[:, :, 2].min()
        self.z_max = trajectories[:, :, 2].max()

        total_frames = trajectories.shape[0]

        n_display_frames = min(
            self.max_animation_frames,
            total_frames
        )

        frame_indices = np.linspace(
            0,
            total_frames - 1,
            n_display_frames,
            dtype=int
        )

        self.displayed_frames = (
            trajectories[frame_indices]
        )

        n_particles = (
            trajectories.shape[1]
        )

        self.particle_selector.setMaximum(
            n_particles
        )
        self.particle_selector.setValue(
            min(10, n_particles)
        )

        self.current_frame = 0

        print(
            "Original:",
            trajectories.shape
        )

        print(
            "Displayed:",
            self.displayed_frames.shape
        )

        self.draw_first_frame()
        self.frame_indices = frame_indices

    def draw_first_frame(self):

        if self.history is None:
            return
        self.current_frame = 0
        frame = self.get_selected_frame()

        self.figure.clear()

        self.ax = self.figure.add_subplot(
            111,
            projection="3d"
        )

        self.scatter = self.ax.scatter(
            frame[:, 0],
            frame[:, 1],
            frame[:, 2]
        )

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")

        self.ax.set_xlim(
            self.x_min,
            self.x_max
        )

        self.ax.set_ylim(
            self.y_min,
            self.y_max
        )

        self.ax.set_zlim(
            self.z_min,
            self.z_max
        )


        self.canvas.draw()
    def update_frame(self):

        if self.displayed_frames is None:
            print("No trajectories available for animation.")
            return

        self.current_frame += 1

        if self.current_frame >= len(
            self.displayed_frames
        ):

            self.timer.stop()
            print("Animation finished.")
            return

        frame = self.get_selected_frame()

        self.scatter._offsets3d = (
            frame[:, 0],
            frame[:, 1],
            frame[:, 2]
        )
        simulated_time = (
            self.frame_indices[
                self.current_frame
            ]
            *
            self.simulation_dt
        )
        self.time_label.setText(
            f"Simulated time: "
            f"{simulated_time:.3f} s"
        )
        print(
            f"Frame {self.current_frame}: "
            f"Simulated time: {simulated_time:.3f} s"
        )
        self.canvas.draw_idle()
    def play_animation(self):

        if self.history is None:
            print("No history available for animation.")
            return

        self.timer.start(33)
    def pause_animation(self):

        self.timer.stop()
    def reset_animation(self):

        self.timer.stop()

        self.current_frame = 0

        self.draw_first_frame()
    def get_selected_frame(self):

        frame = self.displayed_frames[
            self.current_frame
        ]

        n_particles = frame.shape[0]

        requested = (
            self.particle_selector.value()
        )

        if requested >= n_particles:

            return frame

        indices = np.linspace(
            0,
            n_particles - 1,
            requested,
            dtype=int
        )

        return frame[indices]
    def redraw_current_frame(self):

        if self.displayed_frames is None:
            return

        frame = self.get_selected_frame()

        self.scatter._offsets3d = (
            frame[:, 0],
            frame[:, 1],
            frame[:, 2]
        )

        self.canvas.draw_idle()
