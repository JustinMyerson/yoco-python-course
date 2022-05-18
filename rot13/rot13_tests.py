import unittest

from rot13 import rot13


class rot13Tests(unittest.TestCase):

    def test_phrase(self):
        self.assertEqual(rot13("abcde"), "nopqr")

    def test_empty(self):
        self.assertEqual(rot13(""), "")

    def test_uppercase(self):
        self.assertEqual(rot13("HELLO"), "URYYB")

    def test_number(self):
        self.assertEqual(rot13(123), 123)

    def test_mixed(self):
        self.assertEqual(rot13("h2llo"), "u2yyb")

    def test_mixed_start_with_number(self):
        self.assertEqual(rot13("2llo7891keleo"), "2yyb7891xryrb")


if __name__ == '__main__':
    unittest.main()
