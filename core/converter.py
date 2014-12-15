#-*- coding: utf-8 -*-
import string

__all__ = [ 'baseBin', 'baseOct', 'baseHex', 'base62' ]

class Converter(object):
    """
    Converter - Convert from base 10 integer number to base x string back again.

    OBS: This tiny library doesn't work with negative number yet.
         I intend to implement more features like 2`s and 1`s complement.
         Thanks!
    """
    def __init__(self, digits):
        self.digits = digits
        self.length = len(digits)

    def from_decimal(self, number):
        """
        from_decimal() - convert from base 10 integer numbers to base x strings

        :param number: an integer base 10
        """
        if number < 0:
            raise ValueError("The number must be an positive integer!")

        encoded = ''

        while number >= self.length:
            number, mod = divmod(number, self.length)
            encoded = self.digits[mod] + encoded

        encoded = self.digits[number] + encoded

        return encoded

    def to_decimal(self, s):
        """
        to_decimal() - convert from base x strings to base 10 integer numbers

        :param s: a string base x
        """
        decoded = 0
        for char in str(s):
            decoded = decoded * self.length + self.digits.index(char)
        return decoded

baseBin = Converter('01')
baseOct = Converter('01234567')
baseHex = Converter('0123456789ABCDEF')
base62  = Converter(string.digits + string.letters)