from physics.beam import Beam

from physics.field_function import (
    FieldFunction
)

from physics.vector_field import (
    VectorField
)

from components.EM_module import (
    EM_Module
)

from analysis.beam_history import (
    BeamHistory
)

from simulation.engine import (
    SimulationEngine
)
import matplotlib.pyplot as plt
from graphics.plot import plot_trajectory_projections

beam = Beam.gaussian_beam(
    n_particles=100,
    position_mean=(0, 0, 0.5),
    velocity_mean=(0, 0, 5),
    q_over_m=1
)


Ex = FieldFunction(
    "50*sin(pi*z)*cos(t)"
)
Ey = FieldFunction(
    "25*x*y"
)
Ez = FieldFunction(
    "100*exp(-(x**2+y**2))*sin(3*t)"
)

E_field = VectorField(
    Ex,
    Ey,
    Ez
)


# Null magnetic field
Bx = FieldFunction(
    "0.1*cos(pi*y)"
)
By = FieldFunction(
    "0.1*sin(pi*x)"
)
Bz = FieldFunction(
    "0.05*z"
)

B_field = VectorField(
    Bx,
    By,
    Bz
)


module = EM_Module(
    name="Accelerator",
    z_min=0,
    z_max=100,
    e_field=E_field,
    b_field=B_field
)


history = BeamHistory()

engine = SimulationEngine(
    beam,
    [module],
    history
)

engine.run(
    n_steps=1000,
    dt=0.001
)

print(
    beam.positions
)

print(
    beam.velocities
)

print(
    history.get_trajectories().shape
)



traj = history.get_trajectories()

plot_trajectory_projections(traj)

fig = plt.figure(
    figsize=(10, 8)
)

ax = fig.add_subplot(
    111,
    projection="3d"
)

for particle in range(
    traj.shape[1]
):

    x = traj[:, particle, 0]
    y = traj[:, particle, 1]
    z = traj[:, particle, 2]

    ax.plot(
        x,
        y,
        z
    )

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_title(
    "3D Particle Trajectories"
)

plt.show()