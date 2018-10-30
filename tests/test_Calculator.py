import unittest
from PythonExercise import Calculator


class test_Calculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator.Calculator()

    def test_is_power_of_two__Input_2_Return_True(self):
        self.assertTrue(self.calculator.is_power_of_two(2))

    def test_is_power_of_two__Input_3_Return_False(self):
        self.assertFalse(self.calculator.is_power_of_two(3))

    def test_is_power_of_two__Input_4_Return_True(self):
        self.assertTrue(self.calculator.is_power_of_two(4))

    def test_is_power_of_two__Input_0_Return_False(self):
        self.assertFalse(self.calculator.is_power_of_two(0))
