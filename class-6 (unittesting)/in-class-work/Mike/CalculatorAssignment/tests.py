import unittest
from calculator.operations import *

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        print "Test Started"

    def test_add(self):
        """Should return 3 when summing 1 and 2"""
        self.assertEqual(add(1,2), 3)
        
    def test_subtract(self):
        """Should return 1 when subtracting 1 from 2"""
        self.assertEqual(subtract(2,1), 1)

    def test_square(self):
        """Should return 4 when squarring 2"""
        self.assertEqual(square(2), 4)
        
    def test_multiply(self):
        """Should return 6 when multiplying 2 and 3"""
        self.assertEqual(multiply(2,3), 6)

    def tearDown(self):
        print "Test Complete"

if __name__ == "__main__":
    unittest.main()
    




