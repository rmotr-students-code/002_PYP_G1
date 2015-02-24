import unittest
from calculator.operations import *

class OperationsTest(unittest.TestCase):
    
    def setUp(self):
        self.number1 = 20 
        self.number2 = 10
        
    def test_findsum(self):
        """Should return 30 when given number1 and number2"""
        self.assertEqual(find_sum(self.number2, self.number1), 30)
        
    def test_subtract(self):
        """Should return 10 when given number1 and number2"""
        self.assertEqual(subtract(self.number1, self.number2), 10)
    # it runs setup and teardown EVERYTIME? not sure
    
        
if __name__ == '__main__':
    unittest.main()