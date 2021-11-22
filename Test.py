#!/usr/bin/python3
# Test case for finding difference between two numbers
import unittest

from Difference import difference

class TestSum(unittest.TestCase):
    def test_list_int(self):
        
        x=23, y=32
        result = difference(data)
        self.assertEqual(result, 9)

    def test_list_int(self):
        
        x=2, y=3
        result = difference(data)
        self.assertEqual(result, 1)

    def test_list_int(self):
       
        x=100, y=5
        result = difference(data)
        self.assertEqual(result, 95)

if __name__ == '__main__':
    unittest.main()
