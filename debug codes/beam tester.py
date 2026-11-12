from physics.beam import Beam

import matplotlib.pyplot as plt

beam = Beam.gaussian_beam(
    n_particles=100,
    velocity_mean=(0, 0, 100)
)

print(beam.n_particles)

print(beam.positions[:5])
print(beam.velocities[:5])
print(beam.mean_position())
print(beam.mean_velocity())
print(beam.velocity_magnitude()[:5])

plt.scatter(
    beam.positions[:,0],
    beam.positions[:,2],
    s=5
)

plt.xlabel("x")
plt.ylabel("z")

plt.show()
