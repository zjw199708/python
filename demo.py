import unittest
from selectuser import TestBankSelectUser
from takemoney import  TestBanktakemoney
from transformmoney import TestBanktransformmoney
from savemoney import TestBanksavemoney
from adduser import TestBankadduser
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()

suite.addTest(TestBankadduser('testAdduser'))
suite.addTest(TestBankadduser('testAdduser1'))
suite.addTest(TestBankadduser('testAdduser2'))
suite.addTest(TestBanksavemoney('testSaveMoney'))
suite.addTest(TestBanktakemoney('testTakeMoney'))
suite.addTest(TestBanktakemoney('testTakeMoney1'))
suite.addTest(TestBanktakemoney('testTakeMoney2'))
suite.addTest(TestBanktakemoney('testTakeMoney3'))
suite.addTest(TestBanktransformmoney('testTransform'))
suite.addTest(TestBanktransformmoney('testTransform1'))
suite.addTest(TestBanktransformmoney('testTransform2'))
suite.addTest(TestBanktransformmoney('testTransform3'))
suite.addTest(TestBankSelectUser('testBankSelectUser'))

f = open('银行.html','w+',encoding='utf-8')
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title = '银行测试报告',
    description='这是一个银行的测试',
    verbosity=1,
)
htmlrunner.run(suite)