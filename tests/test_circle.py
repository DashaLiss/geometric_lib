import unittest
import calculate


class TestCircle(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(calculate.calc("circle", "area", [1]),
                         3.141592653589793)
        self.assertEqual(calculate.calc("circle", "area", [0]),
                         0.0)

    def test_area_negative(self):
        error_message = "incorrect data"
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-666])
        self.assertEqual(str(context.exception), error_message)

    def test_perimeter_positive(self):
        self.assertEqual(calculate.calc("circle", "perimeter", [1]),
                         6.283185307179586)
        self.assertEqual(calculate.calc("circle", "perimeter", [0]),
                         0.0)

    def test_perimeter_negative(self):
        error_message = "incorrect data"
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-666])
        self.assertEqual(str(context.exception), error_message)


if __name__ == "__main__":
    unittest.main()
