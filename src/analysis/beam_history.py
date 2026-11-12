from analysis.snapshots import Snapshot
from analysis.profiles import Profile


class BeamHistory:
    """
    Central container for all simulation data.
    """

    def __init__(self):

        self.snapshots = {}

        self.profiles = {}

        self.trajectory_history = []

    def add_snapshot(
        self,
        name,
        beam,
        time
    ):
        """
        Save a complete beam state.
        """

        self.snapshots[name] = Snapshot(
            name=name,
            positions=beam.positions.copy(),
            velocities=beam.velocities.copy(),
            time=time
        )

    def add_trajectory_step(
        self,
        beam
    ):
        """
        Save particle positions at
        the current simulation step.
        """

        self.trajectory_history.append(
            beam.positions.copy()
        )

    def get_trajectories(self):
        """
        Convert trajectory history
        into a NumPy array.

        Shape:
        (n_steps, n_particles, 3)
        """

        import numpy as np

        return np.array(
            self.trajectory_history
        )

    def create_profile(
        self,
        module_name
    ):

        self.profiles[module_name] = (
            Profile()
        )

    def get_profile(
        self,
        module_name
    ):

        return self.profiles[module_name]