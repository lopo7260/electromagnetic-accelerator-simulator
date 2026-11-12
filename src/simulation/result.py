# simulation/result.py

from dataclasses import dataclass


@dataclass
class SimulationResult:

    trajectories: object

    snapshots: dict

    profiles: dict