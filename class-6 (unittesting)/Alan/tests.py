import unittest
import calculator.operations
from calculator import interface

class TestPractice(unittest.TestCase):
    
    def setUp(self):
        print "Start tests...."
        
    def test_operations(self):
        assert calculator.operations.add(1,2,3) == 6
        self.assertEqual(calculator.operations.add(1,2),3)
    
    def test_interface(self):
        self.assertIsInstance(interface.title, str)
    
    def tearDown(self):
        print "All finished!"

if __name__ == '__main__':
    unittest.main()
    
        