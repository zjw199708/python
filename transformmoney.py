import unittest
import yinhang


class TestBanktransformmoney(unittest.TestCase):

    def testTransform(self):
        outputaccount = 123456
        inputaccount = 654321
        outputpassword = 123456
        outputmoney = 2000
        exept = 0
        yinhang.bank['张三'] = {'account': 123456, 'password': 123456, 'money': 5000}
        yinhang.bank['李四'] = {'account': 654321, 'password': 123456, 'money': 200}
        status = yinhang.bank_transformMoney(outputaccount, inputaccount, outputpassword, outputmoney)
        print(status)
        self.assertEqual(exept, status)

    def testTransform1(self):
        outputaccount = 123456
        inputaccount = 654321
        outputpassword = 123456
        outputmoney = 2000
        exept = 1
        yinhang.bank['张三'] = {'account': 888888, 'password': 123456, 'money': 5000}
        yinhang.bank['李四'] = {'account': 785422, 'password': 123456, 'money': 500}
        status = yinhang.bank_transformMoney(outputaccount, inputaccount, outputpassword, outputmoney)
        print(status)
        self.assertEqual(exept,status)

    def testTransform2(self):
        outputaccount = 123456
        inputaccount = 654321
        outputpassword = 123456
        outputmoney = 2000
        exept = 2
        yinhang.bank['张三'] = {'account': 123456, 'password': 888888, 'money': 5000}
        yinhang.bank['李四'] = {'account': 654321, 'password': 123456, 'money': 500}
        status = yinhang.bank_transformMoney(outputaccount, inputaccount, outputpassword, outputmoney)
        print(status)
        self.assertEqual(exept, status)

    def testTransform3(self):
        outputaccount = 123456
        inputaccount = 654321
        outputpassword = 123456
        outputmoney = 2000
        exept = 3
        yinhang.bank['张三'] = {'account': 123456, 'password': 123456, 'money': 500}
        yinhang.bank['李四'] = {'account': 654321, 'password': 123456, 'money': 500}
        status = yinhang.bank_transformMoney(outputaccount, inputaccount, outputpassword, outputmoney)
        print(status)
        self.assertEqual(exept, status)
