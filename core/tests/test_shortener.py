#coding: utf-8
import unittest
from core import converter

class ConverterTest(unittest.TestCase):

    def _test_converter(self, converter):
        nums = xrange(0, 100)
        for before in nums:
            after = converter.to_decimal(converter.from_decimal(before))
            self.assertEqual(before, after)

    def test_binary_converter(self):
        self._test_converter(converter.baseBin)

    def test_octal_converter(self):
        self._test_converter(converter.baseOct)

    def test_hexadecimal_converter(self):
        self._test_converter(converter.baseHex)

    def test_62_converter(self):
        self._test_converter(converter.base62)
