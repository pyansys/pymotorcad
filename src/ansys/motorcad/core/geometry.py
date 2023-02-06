"""Function for ``Motor-CAD geometry`` not attached to Motor-CAD instance."""
from cmath import polar, rect
from math import degrees, radians


def xy_to_rt(x, y):
    """Convert Motor-CAD cartesian coordinates to polar coordinates in degrees.

    Parameters
    ----------
    x : float
        X coordinate value.
    y : float
        Y coordinate value.

    Returns
    -------
    radius : float
        radial coordinate value.
    theta : float
        angular coordinate value.
    """
    rect_coordinates = complex(x, y)

    radius, theta = polar(rect_coordinates)

    return radius, degrees(theta)


def rt_to_xy(radius, theta):
    """Convert Motor-CAD polar coordinates to cartesian coordinates in degrees.

    Parameters
    ----------
    radius : float
        radial coordinate.
    theta : float
        angular coordinate.

    Returns
    -------
    x : float
        X coordinate.
    y : float
        Y coordinate.
    """
    coordinates_complex = rect(radius, radians(theta))

    x = coordinates_complex.real
    y = coordinates_complex.imag

    return x, y
