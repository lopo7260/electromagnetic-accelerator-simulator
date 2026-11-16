import numpy as np



def plot_trajectory_projections(
    figure,
    trajectories
):
    """
    Plot XY, XZ and YZ trajectory projections
    on an existing Matplotlib Figure.
    """

    trajectories = np.asarray(
        trajectories
    )

    if (
        trajectories.ndim != 3
        or trajectories.shape[0] == 0
        or trajectories.shape[2] != 3
    ):

        raise ValueError(
            "Trajectories must have shape "
            "(n_steps, n_particles, 3)."
        )

    figure.clear()

    planes = (

        (
            "XY plane",
            0,
            1,
            "X",
            "Y"
        ),

        (
            "XZ plane",
            0,
            2,
            "X",
            "Z"
        ),

        (
            "YZ plane",
            1,
            2,
            "Y",
            "Z"
        ),
    )

    axes = figure.subplots(
        1,
        len(planes)
    )

    for axis, (
        title,
        first,
        second,
        first_label,
        second_label
    ) in zip(
        axes,
        planes
    ):

        for particle in range(
            trajectories.shape[1]
        ):

            axis.plot(
                trajectories[:, particle, first],
                trajectories[:, particle, second],
                alpha=0.7
            )

        axis.set_xlabel(
            first_label
        )

        axis.set_ylabel(
            second_label
        )

        axis.set_title(
            title
        )

        axis.set_aspect(
            "equal",
            adjustable="datalim"
        )

        axis.grid(True)

    figure.tight_layout()

    return axes

def plot_trajectory_3d(
    figure,
    trajectories
):
    """
    Plot particle trajectories in 3D.
    """

    import numpy as np

    trajectories = np.asarray(
        trajectories
    )

    if (
        trajectories.ndim != 3
        or trajectories.shape[0] == 0
        or trajectories.shape[2] != 3
    ):
        raise ValueError(
            "Trajectories must have shape "
            "(n_steps, n_particles, 3)."
        )

    figure.clear()

    ax = figure.add_subplot(
        111,
        projection="3d"
    )

    for particle in range(
        trajectories.shape[1]
    ):

        x = trajectories[
            :,
            particle,
            0
        ]

        y = trajectories[
            :,
            particle,
            1
        ]

        z = trajectories[
            :,
            particle,
            2
        ]

        ax.plot(
            x,
            y,
            z,
            alpha=0.8
        )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_title(
        "Particle Trajectories"
    )

    figure.tight_layout()

    return ax

def plot_final_beam_scatter(
    figure,
    trajectories
):

    trajectories = np.asarray(
        trajectories
    )

    positions = trajectories[-1]

    figure.clear()

    ax = figure.add_subplot(111)

    ax.scatter(
        positions[:, 0],
        positions[:, 1],
        alpha=0.8
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    ax.set_title(
        "Final Beam Profile"
    )

    ax.grid(True)

    figure.tight_layout()

    return ax
