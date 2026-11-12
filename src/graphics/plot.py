import numpy as np
import matplotlib.pyplot as plt


def plot_trajectory_projections(trajectories):
    trajectories = np.asarray(trajectories)
    if (
        trajectories.ndim != 3
        or trajectories.shape[0] == 0
        or trajectories.shape[2] != 3
    ):
        raise ValueError(
            "Trajectories must have shape (n_steps, n_particles, 3)."
        )

    planes = (
        ("XY plane", 0, 1, "X", "Y"),
        ("XZ plane", 0, 2, "X", "Z"),
        ("YZ plane", 1, 2, "Y", "Z"),
    )
    figure, axes = plt.subplots(
        1,
        len(planes),
        figsize=(18, 6)
    )

    for axis, (title, first, second, first_label, second_label) in zip(
        axes,
        planes
    ):
        axis.plot(
            trajectories[:, :, first],
            trajectories[:, :, second],
            alpha=0.7
        )
        axis.set_xlabel(first_label)
        axis.set_ylabel(second_label)
        axis.set_title(title)
        axis.set_aspect("equal", adjustable="datalim")
        axis.grid(True)

    figure.tight_layout()
    return figure, axes
