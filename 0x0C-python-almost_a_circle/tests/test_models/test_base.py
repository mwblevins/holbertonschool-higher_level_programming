#!/usr/bin/python3
""" BASE TESTING"""
import unittest


class TestBAse(unittest.TestCase):
    def test_init_with_id(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
    
    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        
if __name__ == '__main__':
    unittest.main()
