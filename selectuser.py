import unittest
import yinhang


class TestBankSelectUser(unittest.TestCase):

    def testBankSelectUser(self):
        account = 123456
        password = 123456
        expect = True
        status = yinhang.bank_selectUser(account, password)
        print(status)
        self.assertEqual(expect, status)
