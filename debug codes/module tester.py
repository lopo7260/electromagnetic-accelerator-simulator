from physics.beam import Beam
from physics.field_function import FieldFunction
from physics.vector_field import VectorField

from components.EM_module import EM_Module


# Generate a small beam
beam = Beam.gaussian_beam(
    n_particles=10,
    position_mean=(0, 0, 1.5),
    position_std=(0.1, 0.1, 0.1),
    velocity_mean=(0, 0, 10),
    velocity_std=(1, 1, 1),
    q_over_m=1
)


# Constant electric field
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


# Module occupying 0 <= z <= 1
module = EM_Module(
    name="Debug Module",
    z_min=0.0,
    z_max=1.5,
    e_field=E_field,
    b_field=B_field
)


# Compute accelerations
accelerations = module.acceleration(
    beam,
    t=1.0
)

print("\nPositions:\n")
print(beam.positions)

print("\nVelocities:\n")
print(beam.velocities)

print("\nAccelerations:\n")
print(accelerations)