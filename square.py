def area(a):
    if a >= 0:
        return a * a
    else:
        raise ValueError("incorrect data")

def perimeter(a):
    if a >= 0:
        return 4 * a
    else:
        raise ValueError("incorrect data")
