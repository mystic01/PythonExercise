import unittest
from PythonExercise import Calculator


class test_Calculator(unittest.TestCase):

    def test_is_power_Of_two__Input_2_Return_True(self):
        calculator = Calculator.Calculator()
        actual = calculator.is_power_of_two(2)
        self.assertTrue(actual)
