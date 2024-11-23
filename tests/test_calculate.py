import unittest
from math import pi
from calculate import calc


class TestCalcPerimeter(unittest.TestCase):
    def test_calc_circle_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [666]
        expected_result = 2 * pi * 666

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [4]
        expected_result = 16

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_triangle_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [333, 333, 333]
        expected_result = 999

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)


class TestCalcArea(unittest.TestCase):
    def test_calc_circle_area(self):
        fig = "circle"
        func = "area"
        size = [666]
        expected_result = 666 * 666 * pi

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_square_area(self):
        fig = "square"
        func = "area"
        size = [11]
        expected_result = 121

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)

    def test_calc_triangle_area(self):
        fig = "triangle"
        func = "area"
        size = [9, 12, 15]
        expected_result = 18

        result = calc(fig, func, size)

        self.assertEqual(result, expected_result)


class TestCalcIntegerNegative(unittest.TestCase):
    def test_calc_values_triangle(self):
        fig = "triangle"
        func = "area"
        size = [-1, 0, -909]
        expected_result = "incorrect data"

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_values_circle(self):
        fig = "circle"
        func = "area"
        size = [-1]
        expected_result = "incorrect data"

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_values_square(self):
        fig = "square"
        func = "area"
        size = [-6]
        expected_result = "incorrect data"

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)
