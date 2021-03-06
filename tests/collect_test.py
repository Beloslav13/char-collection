import unittest

from char_collection.collect import CharacterSequence


class MyCollectCharTest(unittest.TestCase):

    def test_normal(self):
        collect = CharacterSequence()
        result = collect.collect(10)
        self.assertEqual(len(result), 10, "Unexpected length returned (10)")

    def test_zero(self):
        collect = CharacterSequence()
        result = collect.collect(0)
        self.assertEqual(result, "ValuerError: length can be from 1 to 75 characters", "in test_zero return not valid")

    def test_big(self):
        collect = CharacterSequence()
        result = collect.collect(999)
        self.assertEqual(result, "ValuerError: length can be from 1 to 75 characters", "in test big return not valid")

    def test_negative(self):
        collect = CharacterSequence()
        result = collect.collect(-1)
        self.assertEqual(result, "ValuerError: length can be from 1 to 75 characters",
                         "in test negative return not valid")

    def test_string(self):
        collect = CharacterSequence()
        result = collect.collect("dsds")
        self.assertEqual(result, "ValuerError: invalid literal for int() with base 10: 'dsds'",
                         "in test string return not valid")

    def test_int_string(self):
        collect = CharacterSequence()
        result = collect.collect("10")
        self.assertEqual(len(result), 10, "in test int string return not valid")


if __name__ == "__main__":
    unittest.main()
