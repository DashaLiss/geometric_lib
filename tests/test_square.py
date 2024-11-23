import unittest
import calculate

class TestSquare(unittest.TestCase):

    def test_area_positive(self):
        res_area_one_positive = calculate.calc("square", "area", [11])
        self.assertEqual(res_area_one_positive, 121)

        res_area_two_positive = calculate.calc("square", "area", [0])
        self.assertEqual(res_area_two_positive, 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "area", [-666])
        self.assertEqual(str(context.exception),
                         "incorrect data")

    def test_perimeter_positive(self):
        res_perimeter_one_positive = calculate.calc("square", "perimeter", [11])
        self.assertEqual(res_perimeter_one_positive, 44)

        res_perimeter_two_positive = calculate.calc("square", "perimeter", [0])
        self.assertEqual(res_perimeter_two_positive, 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "perimeter", [-666])
        self.assertEqual(str(context.exception),
                         "incorrect data")

if __name__ == "__main__":
    unittest.main()