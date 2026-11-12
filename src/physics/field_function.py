import sympy as sp
import numpy as np

from sympy.parsing.sympy_parser import parse_expr


class FieldFunction:
    """
    Represents a scalar field function f(x,y,z,t).

    The expression is stored as a SymPy expression
    and converted to a NumPy-compatible callable.
    """

    def __init__(self, expression: str):

        self.expression = expression

        # Define symbolic variables
        self.x, self.y, self.z, self.t = sp.symbols(
            "x y z t"
        )

        # Parse user expression
        self.sympy_expression = parse_expr(
            expression
        )

        # Create fast numerical function
        self.function = sp.lambdify(
            (
                self.x,
                self.y,
                self.z,
                self.t
            ),
            self.sympy_expression,
            "numpy"
        )

    def evaluate(self, x, y, z, t):

        value = self.function(
        x,
        y,
        z,
        t
    )

    # Expand scalar values to match array size
        if np.isscalar(value):

            return np.full(
            np.shape(x),
            value,
            dtype=float
        )

        return np.asarray(
        value,
        dtype=float
    )

    def __repr__(self):

        return (
            f"FieldFunction("
            f"{self.expression})"
        )