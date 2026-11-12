import numpy as np


class SimulationEngine:
    """
    Main simulation engine.

    Responsibilities:
    - query all active modules
    - compute total acceleration
    - update velocities
    - update positions
    - record trajectories
    """

    def __init__(
        self,
        beam,
        modules,
        history
    ):

        self.beam = beam

        self.modules = modules

        self.history = history

        self.time = 0.0

    def compute_acceleration(self):
        """
        Compute total acceleration generated
        by all modules.
        """

        total_acceleration = np.zeros_like(
            self.beam.positions
        )

        for module in self.modules:

            total_acceleration += (
                module.acceleration(
                    self.beam,
                    self.time
                )
            )

        return total_acceleration

    def step(
        self,
        dt: float
    ):
        """
        Advance simulation by one step.
        """

        acceleration = (
            self.compute_acceleration()
        )

        # Euler integration

        self.beam.velocities += (
            acceleration * dt
        )

        self.beam.positions += (
            self.beam.velocities * dt
        )

        self.time += dt

        self.history.add_trajectory_step(
            self.beam
        )

        return acceleration

    def run(
        self,
        n_steps: int,
        dt: float
    ):
        """
        Run multiple simulation steps.
        """

        for _ in range(n_steps):

            self.step(dt)