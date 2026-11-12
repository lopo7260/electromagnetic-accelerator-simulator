from dataclasses import dataclass, field

from config.module_config import ModuleConfig


@dataclass
class SimulationConfig:
    """
    Stores the complete simulation configuration.
    """

    particles: int

    q_over_m: float

    dt: float

    n_steps: int

    modules: list[ModuleConfig] = field(
        default_factory=list
    )

    def validate(self):
        """
        Validate the configuration.
        """

        if self.particles <= 0:

            raise ValueError(
                "Particles must be greater than zero."
            )

        if self.dt <= 0:

            raise ValueError(
                "Time step must be greater than zero."
            )

        if self.n_steps <= 0:

            raise ValueError(
                "Number of steps must be greater than zero."
            )

        if len(self.modules) == 0:

            raise ValueError(
                "At least one module is required."
            )