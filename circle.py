import math


def area(r):
    if r >= 0:
        return math.pi * r * r
    else:
        raise ValueError("incorrect data")


def perimeter(r):
    if r >= 0:
        return 2 * math.pi * r
    else:
        raise ValueError("incorrect data")
