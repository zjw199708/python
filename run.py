import unittest
from HTMLTestRunner import HTMLTestRunner



suite = unittest.TestSuite()
loder = unittest.defaultTestLoader
cases =loder.discover('D:\\python\day\\testdemo\\testcase',pattern='*.py')
suite.addTest(cases)

f = open('计算器测试报告.html','w+',encoding='utf-8')
runner = HTMLTestRunner.HTMLTestRunner(
    stream= f,
    title= '计算器测试报告',
    description='这是一个计算器测试',
    verbosity=1
)
runner.run(suite)


