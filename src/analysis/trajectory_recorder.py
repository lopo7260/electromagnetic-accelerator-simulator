# analysis/trajectory_recorder.py

import numpy as np


class TrajectoryRecorder:

    def __init__(self):

        self.trajectory_history = []

    def record(self, beam):

        self.trajectory_history.append(
            beam.positions.copy()
        )

    def get_array(self):

        return np.array(
            self.trajectory_history
        )