import unittest
from day.testdemo.cal import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    [1, 2, 3],
    [-1, -4, -5],
    [2, 3, 5]
]


@ddt
class TestCaladd(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self, d, e, f):
        a = d
        b = e
        sum = f
        c = Calc()
        s = c.add(a, b)

        # 断言
        self.assertEqual(sum, s)
