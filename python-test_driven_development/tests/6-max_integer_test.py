#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_only_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([-5, 6, 89, 666, 45, -666, 2]), 666)

    def test_one_element(self):
        self.assertEqual(max_integer([666]), 666)

    def test_multi_types(self):
        self.assertRaises(TypeError, max_integer, list=[5.68, "test_me", 2])

if __name__ == '__main__':
    unittest.main()