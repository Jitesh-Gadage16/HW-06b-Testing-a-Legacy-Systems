import math

def classify_triangle(a, b, c):
    """
    Determines the type of triangle based on given side lengths.

    Parameters:
    a (float): Length of first side
    b (float): Length of second side
    c (float): Length of third side

    Returns:
    str: Type of triangle (Equilateral, Isosceles, Scalene, Right Triangle, or Not a Triangle)
    """

    # Ensure valid side lengths
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a Triangle"

    # Check Triangle Inequality Theorem
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a Triangle"

    # Identify triangle type
    if a == b == c:
        return "Equilateral"

    triangle_type = "Isosceles" if (a == b or b == c or a == c) else "Scalene"

    # Check for Right Triangle using math.isclose()
    if math.isclose(a**2 + b**2, c**2, rel_tol=1e-5) or \
       math.isclose(a**2 + c**2, b**2, rel_tol=1e-5) or \
       math.isclose(b**2 + c**2, a**2, rel_tol=1e-5):
        return f"{triangle_type} and Right Triangle"

    return triangle_type
