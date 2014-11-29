#coding: utf-8
import unittest
from shortener import converter

class ConverterTest(unittest.TestCase):

    def _test_converter(self, converter):
        nums = xrange(0, 1000)
        for before in nums:
            asc = converter.from_decimal(before)
            after = converter.to_decimal(converter.from_decimal(before))
            print asc, after
            self.assertEqual(before, after)

    def test_converter(self):
        self._test_converter(converter.base64)
