import numpy as np


UP = np.loadtxt("../resources/spring_up.csv", delimiter=",", dtype=float)
DOWN = np.loadtxt("../resources/spring_down.csv", delimiter=",", dtype=float)


def sample_force(displacement: float, velocity: float) -> float:
    """
    Calculates the force on a spring given its displacement and vertical velocity.

    Args:
        velocity (float): The vertical velocity of the leaf spring.
        displacement (float): The vertical displacement of the leaf spring.

    Returns:
        float: The force on the leaf spring.
    """

    if velocity > 0:
        if displacement < 0 or displacement > UP[-1, 0]:
            raise ValueError("Displacement out of range.")

        if abs(displacement) < 0.0001:
            return UP[0, 1]
        if abs(displacement - UP[-1, 0]) < 0.0001:
            return UP[-1, 1]

        i = np.searchsorted(UP[:, 0], displacement)
        f = (displacement - UP[i - 1, 0]) / (UP[i, 0] - UP[i - 1, 0])
        y = ((1 - f) * UP[i - 1, 1]) + (f * UP[i, 1])
        return y

    if displacement < 0 or displacement > DOWN[-1, 0]:
        raise ValueError("Displacement out of range.")

    i = np.searchsorted(DOWN[:, 0], displacement)
    f = (displacement - DOWN[i - 1, 0]) / (DOWN[i, 0] - DOWN[i - 1, 0])
    y = ((1 - f) * DOWN[i - 1, 1]) + (f * DOWN[i, 1])
    return y
