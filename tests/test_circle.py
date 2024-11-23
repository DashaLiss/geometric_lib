import unittest
import calculate

class TestCircle(unittest.TestCase):

    def test_area_positive(self):
        res_area_one_positive = calculate.calc("circle", "area", [1])
        self.assertEqual(res_area_one_positive, 3.141592653589793)

        res_area_two_positive = calculate.calc("circle", "area", [0])
        self.assertEqual(res_area_two_positive, 0.0)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-666])
        self.assertEqual(str(context.exception),
                         "incorrect data")

    def test_perimeter_positive(self):
        res_perimeter_one_positive = calculate.calc("circle", "perimeter", [666])
        self.assertEqual(res_perimeter_one_positive, 4184.601414581604)

        res_perimeter_two_positive = calculate.calc("circle", "perimeter", [0])
        self.assertEqual(res_perimeter_two_positive, 0.0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-666])
        self.assertEqual(str(context.exception),
                         "incorrect data")

if __name__ == "__main__":
    unittest.main()