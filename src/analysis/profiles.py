from dataclasses import dataclass
import numpy as np

@dataclass
class Profile:
    """
    Represent a system profile sampled along its traveled distance.

    ``mean_position``, ``mean_velocity``, and ``mean_acceleration`` are
    expected to have shape ``(N, 3)``. With float64 components, each
    three-component element is 192 bits (24 bytes). ``s`` and ``rms_radius``
    are expected to contain one float64 scalar per sample (64 bits / 8 bytes).
    """

    s: np.ndarray

    mean_position: np.ndarray

    mean_velocity: np.ndarray

    mean_acceleration: np.ndarray

    rms_radius: np.ndarray