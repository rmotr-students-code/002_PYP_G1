import unittest
from calculator.operations import add, subs, multiply, divide

class TestOps(unittest.TestCase):
    
    def setUp(self):
        print("start testing")
    
    def test_add(self):
        """Should return 4 when summing 2 and 2 """
        self.assertEqual(add(2,2),4)
        
    def test_subs(self):
        """Should return 2 when substracting 2 from 4"""
        self.assertEqual(subs(4,2),2)
        
    def test_multiply(self):
        """Should return 9 when we multiply 3 and 3"""
        self.assertEqual(multiply(3,3),9)
        
    def test_divide(self):
        """Should return 5 when we devide 10 by 2"""
        self.assertEqual(divide(10,2),5)
    
    def tearDown(self):
        print("test complete")
        
if __name__ == "__main__":
    unittest.main()