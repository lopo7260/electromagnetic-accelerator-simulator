from physics.beam import Beam

from physics.field_function import FieldFunction
from physics.vector_field import VectorField

from components.EM_module import EM_Module

from analysis.beam_history import BeamHistory

from simulation.engine import SimulationEngine


class SimulationBuilder:

    @staticmethod
    def build(config):
        
        modules = []

        for module_config in config.modules:

            e_field = VectorField(
                FieldFunction(module_config.Ex),
                FieldFunction(module_config.Ey),
                FieldFunction(module_config.Ez)
            )

            b_field = VectorField(
                FieldFunction(module_config.Bx),
                FieldFunction(module_config.By),
                FieldFunction(module_config.Bz)
            )

            module = EM_Module(
                name=module_config.name,
                z_min=module_config.z_min,
                z_max=module_config.z_max,
                e_field=e_field,
                b_field=b_field
            )

            modules.append(module)

        beam = Beam.gaussian_beam(
            n_particles=config.particles,
            q_over_m=config.q_over_m
        )

        history = BeamHistory()

        engine = SimulationEngine(
            beam=beam,
            modules=modules,
            history=history
        )

        return engine