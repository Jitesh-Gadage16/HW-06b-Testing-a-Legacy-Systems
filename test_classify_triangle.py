import unittest
import math
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    # Equilateral Triangle
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    # Isosceles Triangles (Including Right Isosceles)
    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")
        self.assertEqual(classify_triangle(8, 5, 5), "Isosceles")

    def test_isosceles_right_triangle(self):
        self.assertEqual(classify_triangle(5, 5, math.sqrt(50)), "Isosceles and Right Triangle")

    # Scalene Triangles (Including Right Scalene)
    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(7, 8, 9), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right Triangle")

    # Edge Cases
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 2), "Not a Triangle")
        self.assertEqual(classify_triangle(10, 2, 2), "Not a Triangle")

    def test_negative_values(self):
        self.assertEqual(classify_triangle(-3, 4, 5), "Not a Triangle")
        self.assertEqual(classify_triangle(-1, -1, -1), "Not a Triangle")

    def test_zero_values(self):
        self.assertEqual(classify_triangle(0, 0, 0), "Not a Triangle")
        self.assertEqual(classify_triangle(0, 5, 5), "Not a Triangle")

    def test_floating_point_precision(self):
        self.assertEqual(classify_triangle(0.3, 0.4, 0.5), "Scalene and Right Triangle")

    def test_large_values(self):
        self.assertEqual(classify_triangle(1e100, 1e100, 1e100), "Equilateral")

    def test_minimum_positive_values(self):
        self.assertEqual(classify_triangle(0.0001, 0.0001, 0.0001), "Equilateral")

if __name__ == "__main__":
    unittest.main()
