from dataclasses import dataclass
import numpy as np


@dataclass
class Snapshot:
    """
    Complete state of the beam at a specific point.
    """

    name: str

    positions: np.ndarray
    velocities: np.ndarray

    time: float