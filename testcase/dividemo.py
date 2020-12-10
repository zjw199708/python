import unittest
from day.testdemo.cal import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [10,5,2],
    [36,6,6],
    [20,4,5]
]

@ddt
class TestCaldivide(unittest.TestCase):
    @data(*data1)
    @unpack
    def testdivi(self,d,e,f):
        a = d
        b = e
        expect = f
        calc = Calc()

        divi = calc.divi(a,b)

        self.assertEqual(expect,divi)