from physics.beam import Beam
from analysis.beam_history import BeamHistory

beam = Beam.gaussian_beam(
    n_particles=10
)

history = BeamHistory()

history.add_snapshot(
    "source",
    beam,
    time=0
)

history.add_trajectory_step(
    beam
)

print(
    history.snapshots.keys()
)

print(
    history.get_trajectories().shape
)