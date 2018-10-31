import unittest
from PythonExercise import Parser


class test_Parser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser.Parser()

    def test_ParseVersionString_normal_case(self):
        product_info = self.parser.Parse("PLC320-1810310001(1.05)")
        self.assertEqual("PLC320", product_info.model_name)
        self.assertEqual("1810310001", product_info.date_code)
        self.assertEqual("1", product_info.major_version)
        self.assertEqual("0.5", product_info.minor_version)

    def test_ParseVersionString_error_case_return_none(self):
        product_info = self.parser.Parse("PLC320-1810310001(1.05))")
        self.assertIsNone(product_info)

    def test_ParseVersionString_error_case2_return_none(self):
        product_info = self.parser.Parse("PLC320--1810310001(1.05)")
        self.assertIsNone(product_info)
