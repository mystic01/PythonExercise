import unittest
from PythonExercise import Parser


class test_Parser(unittest.TestCase):

    def test_ParseVersionString(self):
        parser = Parser.Parser()
        model_name, date_code, major_version, minor_version = parser.Parse(
            "PLC320-1810310001(1.05)")
        self.assertEqual("PLC320", model_name)
        self.assertEqual("1810310001", date_code)
        self.assertEqual("1", major_version)
        self.assertEqual("0.5", minor_version)
