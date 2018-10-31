import unittest
from PythonExercise import Parser


class test_Parser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser.Parser()

    def test_ParseVersionString_normal_case(self):
        model_name, date_code, major_version, minor_version = self.parser.Parse(
            "PLC320-1810310001(1.05)")
        self.assertEqual("PLC320", model_name)
        self.assertEqual("1810310001", date_code)
        self.assertEqual("1", major_version)
        self.assertEqual("0.5", minor_version)

    def test_ParseVersionString_error_case_return_none(self):
        result = self.parser.Parse("PLC320-1810310001(1.05))")
        self.assertIsNone(result)
