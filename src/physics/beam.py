from dataclasses import dataclass
import numpy as np


@dataclass
class Beam:
    """
    A class representing a beam of particles.
    including their positions, velocities, and charge-to-mass ratio.
    and methods to generate a Gaussian beam of particles.
    """

    positions: np.ndarray
    velocities: np.ndarray
    q_over_m: float

    @property
    def n_particles(self):
        return len(self.positions)

    @staticmethod
    def gaussian_beam(
        n_particles: int,
        position_mean=(0, 0, 0),
        position_std=(1e-3, 1e-3, 1e-3),
        velocity_mean=(0, 0, 10),
        velocity_std=(1, 1, 2),
        q_over_m=-1.0,
    ):

        positions = np.random.normal(
            loc=position_mean,
            scale=position_std,
            size=(n_particles, 3)
        )

        velocities = np.random.normal(
            loc=velocity_mean,
            scale=velocity_std,
            size=(n_particles, 3)
        )

        return Beam(
            positions=positions,
            velocities=velocities,
            q_over_m=q_over_m
        )
    def mean_position(self):
        return np.mean(self.positions, axis=0)

    def mean_velocity(self):
        return np.mean(self.velocities, axis=0)
    
    def velocity_magnitude(self):
        return np.linalg.norm(
            self.velocities,
            axis=1
        )