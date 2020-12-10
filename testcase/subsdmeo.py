import unittest
from day.testdemo.cal import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [
    [10, 5, 5],
    [20, 1, 19],
    [5, 2, 3]
]


@ddt
class TestCalsubs(unittest.TestCase):
    @data(*data1)
    @unpack
    def testSubs(self, d, e, f):
        a = d
        b = e
        sub = f
        c = Calc()
        s = c.subs(a, b)

        # 断言
        self.assertEqual(sub, s)
