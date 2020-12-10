import unittest
import yinhang


class TestBanktakemoney(unittest.TestCase):

    def testTakeMoney(self):
        account = 123456
        password = 123456
        money = 1000
        expect = 0
        yinhang.bank['张三'] = {'account': 123456, 'password': 123456, 'money': 5000}
        status = yinhang.bank_takeMoney(account, password, money)

        print(status)

        self.assertEqual(expect,status)

    def testTakeMoney1(self):
        account = 123456
        password = 123456
        money = 6000
        expect = 3
        yinhang.bank['张三'] = {'account': 123456, 'password': 123456, 'money': 5000}
        status = yinhang.bank_takeMoney(account, password, money)
        print(status)
        self.assertEqual(expect,status)

    def testTakeMoney2(self):
        account = 123456
        password = 123456
        money = 6000
        expect = 2
        yinhang.bank['张三'] = {'account': 123456, 'password': 654321, 'money': 5000}
        status = yinhang.bank_takeMoney(account, password, money)

        print(status)

        self.assertEqual(expect, status)

    def testTakeMoney3(self):
        account = 123456
        password = 123456
        money = 6000
        expect = 1
        yinhang.bank['张三'] = {'account': 654321, 'password': 123456, 'money': 5000}
        status = yinhang.bank_takeMoney(account, password, money)

        print(status)

        self.assertEqual(expect, status)
