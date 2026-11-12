import numpy as np

from physics.vector_field import VectorField


class EM_Module:
    """
    Generic electromagnetic module.

    The module acts only on particles
    inside its spatial region.

    It computes the Lorentz acceleration
    but does not update the beam state.
    """

    def __init__(
        self,
        name: str,
        z_min: float,
        z_max: float,
        e_field: VectorField,
        b_field: VectorField
    ):

        self.name = name

        self.z_min = z_min
        self.z_max = z_max

        self.e_field = e_field
        self.b_field = b_field

    @property
    def length(self):

        return (
        self.z_max
        -
        self.z_min
    )

    def particle_mask(self, beam):
        """
        Return particles contained
        inside the module.
        """

        z = beam.positions[:, 2]

        return (
            (z >= self.z_min)
            &
            (z <= self.z_max)
        )

    def contains(self, z):

        return (
        self.z_min
        <= z
        <= self.z_max
    )

    def acceleration(
        self,
        beam,
        t: float
    ):
        """
        Compute acceleration generated
        by this module.

        Returns:
        --------
        acceleration : ndarray(N,3)

        Particles outside the module
        receive zero acceleration.
        """

        acceleration = np.zeros_like(
            beam.positions
        )

        mask = self.particle_mask(
            beam
        )

        if not np.any(mask):
            return acceleration

        positions = beam.positions[mask]
        velocities = beam.velocities[mask]

        x = positions[:, 0]
        y = positions[:, 1]
        z = positions[:, 2]

        E = self.e_field.evaluate(
            x,
            y,
            z,
            t
        )

        B = self.b_field.evaluate(
            x,
            y,
            z,
            t
        )

        acceleration[mask] = (
            beam.q_over_m
            *
            (
                E
                +
                np.cross(
                    velocities,
                    B
                )
            )
        )

        return acceleration