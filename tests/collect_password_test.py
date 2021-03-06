import unittest

from char_collection.collect_password import CollectPassword


class MyCollectCharTest(unittest.TestCase):

    def test_normal(self):
        collect = CollectPassword()
        result = collect.collect(10)
        self.assertEqual(len(result), 10, 'Unexpected length returned (10)')

    def test_zero(self):
        collect = CollectPassword()
        result = collect.collect(0)
        self.assertEqual(result, "ValuerError: password length can be from 6 to 20 characters",
                         'in test_zero return not valid')

    def test_big(self):
        collect = CollectPassword()
        result = collect.collect(999)
        self.assertEqual(result, "ValuerError: password length can be from 6 to 20 characters",
                         'in test big return not valid')

    def test_negative(self):
        collect = CollectPassword()
        result = collect.collect(-1)
        self.assertEqual(result, "ValuerError: password length can be from 6 to 20 characters",
                         'in test negative return not valid')

    def test_string(self):
        collect = CollectPassword()
        result = collect.collect('dsds')
        self.assertEqual(result, "ValuerError: invalid literal for int() with base 10: 'dsds'",
                         'in test string return not valid')

    def test_int_string(self):
        collect = CollectPassword()
        result = collect.collect('10')
        self.assertEqual(len(result), 10, 'in test int string return not valid')


if __name__ == '__main__':
    unittest.main()
