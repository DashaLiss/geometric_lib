def area(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return (a + b + c) / 2
    else:
        raise ValueError("incorrect data")


def perimeter(a, b, c):
    if a >= 0 and b >= 0 and c >= 0:
        return a + b + c
    else:
        raise ValueError("incorrect data")
