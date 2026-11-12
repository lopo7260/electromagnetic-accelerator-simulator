from dataclasses import dataclass
import numpy as np

from analysis import profiles

class PlotData:

    @staticmethod
    def xy_scatter(snapshot):   
        return (
        snapshot.positions[:,0],
        snapshot.positions[:,1]
    )

    @staticmethod
    def xz_scatter(snapshot):
        return (
        snapshot.positions[:,0],
        snapshot.positions[:,2]
    )

    @staticmethod
    def yz_scatter(snapshot):
        return (
        snapshot.positions[:,1],
        snapshot.positions[:,2]
    )

    @staticmethod
    def speed_distribution(snapshot):

        return np.linalg.norm(
        snapshot.velocities,
        axis=1
    )

    @staticmethod
    def kinetic_energy_over_q(snapshot,q_over_m):
        speed = np.linalg.norm(
            snapshot.velocities,
            axis=1
        )
        return (
            0.5 * q_over_m**-1 *  speed**2
    )

    @staticmethod
    def rms_radius(profile):
        return (
        profile.s,
        profile.rms_radius
    )