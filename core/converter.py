#coding: utf-8
import string

__all__ = [ 'base62', ]

class Converter(object):
    """
    Converter - Convert from base 10 integer number to base x string back again
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
            number, negative = -number, 1
        else:
            negative = 0

        encoded = ''

        while number >= self.length:
            number, mod = divmod(number, self.length)
            encoded = self.digits[mod] + encoded

        encoded = self.digits[number] + encoded

        if negative:
            encoded = '-' + encoded
        return encoded

    def to_decimal(self, s):
        """
        to_decimal() - convert from base x strings to base 10 integer numbers

        :param s: a string base x
        """
        s = str(s)

        if s[0] == '-':
            s, negative = s[1:], 1
        else:
            negative = 0

        decoded = 0
        m = 1

        while len(s) > 0:
            decoded += m * self.digits.index(s[-1:])
            m = m * self.length
            s = s[:-1]

        if negative:
            decoded = -decoded
        return decoded

ascii62 = string.digits + string.letters

base62 = Converter(ascii62)