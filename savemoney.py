import unittest
import yinhang

class TestBanksavemoney(unittest.TestCase):

    def testSaveMoney(self):

        acount = 123456
        money = 1000
        exept = True
        status = yinhang.bank_saveMoney(acount,money)
        print(status)
        #断言
        self.assertEqual(exept,status)