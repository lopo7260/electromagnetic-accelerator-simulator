from physics.beam import Beam

from physics.field_function import (
    FieldFunction
)

from physics.vector_field import (
    VectorField
)

from components.EM_module import (
    EMModule
)

from analysis.beam_history import (
    BeamHistory
)

from simulation.engine import (
    SimulationEngine
)


class SimulationBuilder:
    """
    Convert a SimulationConfig into a
    fully initialized simulation.
    """

    @staticmethod
    def build(simulation_config):

        modules = []

        for module_config in simulation_config.modules:

            ex = FieldFunction(
                module_config.Ex
            )

            ey = FieldFunction(
                module_config.Ey
            )

            ez = FieldFunction(
                module_config.Ez
            )

            bx = FieldFunction(
                module_config.Bx
            )

            by = FieldFunction(
                module_config.By
            )

            bz = FieldFunction(
                module_config.Bz
            )

            e_field = VectorField(
                ex,
                ey,
                ez
            )

            b_field = VectorField(
                bx,
                by,
                bz
            )

            module = EMModule(
                name=module_config.name,

                z_min=module_config.z_min,
                z_max=module_config.z_max,

                e_field=e_field,
                b_field=b_field
            )

            modules.append(
                module
            )

        beam = Beam.gaussian_beam(

            n_particles=
            simulation_config.particles,

            q_over_m=
            simulation_config.q_over_m
        )

        history = BeamHistory()

        engine = SimulationEngine(

            beam=beam,

            modules=modules,

            history=history
        )

        return engine