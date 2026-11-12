import numpy as np

from .field_function import FieldFunction


class VectorField:
    """
    Represents a vector field:

    F = (Fx, Fy, Fz)

    where each component is a
    FieldFunction.
    """

    def __init__(
        self,
        fx: FieldFunction,
        fy: FieldFunction,
        fz: FieldFunction
    ):

        self.fx = fx
        self.fy = fy
        self.fz = fz

    def evaluate(
        self,
        x,
        y,
        z,
        t
    ):
        """
        Evaluate field components.
        """

        Fx = self.fx.evaluate(
            x, y, z, t
        )

        Fy = self.fy.evaluate(
            x, y, z, t
        )

        Fz = self.fz.evaluate(
            x, y, z, t
        )

        return np.column_stack(
            (
                Fx,
                Fy,
                Fz
            )
        )