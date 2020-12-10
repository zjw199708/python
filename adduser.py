import unittest
import yinhang


class TestBankadduser(unittest.TestCase):

    def testAdduser(self):
        username = '张岩'
        password = 123456
        country = '中国'
        province = '内蒙'
        street = '同福客栈'
        door = 12138
        money = 1000
        account = 123456
        expect = 2
        yinhang.bank['张岩'] = {'account': 123456, 'password': 123456, 'country': '中国',
                              'province': '内蒙', 'street': '同福客栈'}
        status = yinhang.bank_addUser(username, password, country, province, street, door, money)
        print(status)
        self.assertEqual(expect, status)

    def testAdduser1(self):
        username = None
        password = None
        country = None
        province = None
        street = None
        door = None
        money = None
        expect = 1
        status = yinhang.bank_addUser(username, password, country, province, street, door, money)
        print(status)
        self.assertEqual(expect, status)

    def testAdduser2(self):
        username = None
        password = None
        country = None
        province = None
        street = None
        door = None
        money = None
        expect = 3

        for i in range(100):
            yinhang.bank['张三' + str(i)] = {}
        status = yinhang.bank_addUser(username, password, country, province, street, door, money)
        print(status)
        self.assertEqual(expect, status)
