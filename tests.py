import unittest
from parking_calc import FeesCalculator


class FeesCalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        case_1 = FeesCalculator()
        case_2 = FeesCalculator()
        case_3 = FeesCalculator()
        case_4 = FeesCalculator()
        self.case_5 = FeesCalculator()
        self.case_6 = FeesCalculator()
        self.case_1 = case_1.calc('10:30', '12:31')
        self.case_2 = case_2.calc('14:29', '18:11')
        self.case_3 = case_3.calc('09:01', '10:00')
        self.case_4 = case_4.calc('17:40', '23:40')

    def test_positive_test(self):
        self.assertEqual(13, self.case_1)
        self.assertEqual(17, self.case_2)
        self.assertEqual(5, self.case_3)
        self.assertEqual(25, self.case_4)

    def test_negative_test(self):
        self.assertNotEqual(10, self.case_1)
        self.assertNotEqual(1, self.case_2)
        self.assertNotEqual(2, self.case_3)
        self.assertNotEqual(22, self.case_4)

    def test_output_error(self):
        try:
            self.case_5.str_to_datetime_object('17:40:00')
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

        try:
            self.case_6.str_to_datetime_object('17/05/2023 17:40:00')
        except ValueError as error:
            self.assertEqual(type(error), ValueError)


unittest.main()
