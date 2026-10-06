def perimeter(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3


def semiperimeter(side1: float, side2: float, side3: float) -> float:
    """Return the semiperimeter of a triangle with sides
    side1, side2, and side3.

    >>> semiperimeter(3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    """
    return perimeter(side1, side2, side3) / 2