import unittest
import calculate


class TestTriangle(unittest.TestCase):

    def test_area_positive(self):
        res_area_1_pos = calculate.calc("triangle", "area", [1, 2, 3])
        self.assertEqual(res_area_1_pos, 3)

        res_area_2_pos = calculate.calc("triangle", "area", [0, 0, 0])
        self.assertEqual(res_area_2_pos, 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "area", [-1, -2, -3])
        self.assertEqual(str(context.exception),
                         "incorrect data")

    def test_perimeter_positive(self):
        res_perimeter_1_pos = calculate.calc("triangle",
                                             "perimeter", [1, 2, 3])
        self.assertEqual(res_perimeter_1_pos, 6)

        res_perimeter_2_pos = calculate.calc("triangle",
                                             "perimeter", [0, 0, 0])
        self.assertEqual(res_perimeter_2_pos, 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "perimeter", [-1, -2, -3])
        self.assertEqual(str(context.exception),
                         "incorrect data")


if __name__ == "__main__":
    unittest.main()
