class TriangleType:
    scalene = "scalene"
    isosceles = "isosceles"
    equilateral = "equilateral"


def get_triangle_type(a: float, b: float, c: float) -> str:
    if a == b == c:
        return TriangleType.equilateral
    elif a == b:
        return TriangleType.isosceles
    else:
        return TriangleType.scalene
