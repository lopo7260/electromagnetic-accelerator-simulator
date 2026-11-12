from dataclasses import dataclass


@dataclass
class ModuleConfig:
    """
    Stores the user configuration of a module.

    This class is GUI-friendly and independent
    from the simulation backend.
    """

    name: str

    z_min: float
    z_max: float

    Ex: str
    Ey: str
    Ez: str

    Bx: str
    By: str
    Bz: str