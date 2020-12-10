import unittest
from day.testdemo.cal import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    [2, 2, 4],
    [3, 4, 12],
    [6, 6, 36]
]


@ddt
class TestCalcmult(unittest.TestCase):
    @data(*data1)
    @unpack
    def testMult(self, d, e, f):
        a = d
        b = e
        expect = f
        calc = Calc()
        mul = calc.mult(a, b)

        self.assertEqual(expect, mul)
