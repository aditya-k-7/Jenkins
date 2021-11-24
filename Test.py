#!/usr/bin/python3
# Test case for finding difference between two numbers
import unittest

from Difference import difference

class TestSum(unittest.TestCase):
    def test_list_int(self):
        
        result = difference(23,32)
        self.assertEqual(result, 9)
        
        result = difference(2,3)
        self.assertEqual(result, 1)

        result = difference(100,5)
        self.assertEqual(result, 90)

if __name__ == '__main__':
    unittest.main()
