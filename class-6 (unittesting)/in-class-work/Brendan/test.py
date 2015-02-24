import unittest
from calculator import operations

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        print 'Beginning test'
    
    def test_sum(self):
        """Check that inputs are integers"""
        self.assertEqual(operations.sum_(1,2), 3)
    
    def test_divide(self):
        pass
        """
    
    def tearDown(self):
        print 'Ending test'
    """
if __name__ == '__main__':
    unittest.main()