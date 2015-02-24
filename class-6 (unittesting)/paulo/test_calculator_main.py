import unittest
import calculator_main


class Test_calculator(unittest.TestCase):

    def setUp(self):
        """This function is run before each test"""
        pass
    
    def test_calculator_sum(self):
        """tests the sum function"""
        #should... when...  -> change this
        observed = calculator_main.calculator_sum(2,3)
        expected = 5
        self.assertEqual(observed, expected)

    def test_calculator_subtract(self):
        """tests the subtract function"""
        observed = calculator_main.calculator_subtract(-1,-1)
        expected = 0
        self.assertEqual(observed, expected)

    def test_calculator_divide(self):
        """tests the divide function"""
        observed = calculator_main.calculator_divide(10,-2)
        expected = -5
        self.assertEqual(observed, expected)
    
    def test_calculator_multiply(self):
        """tests the multiply function"""
        observed = calculator_main.calculator_multiply(10,-2)
        expected = -20
        self.assertEqual(observed, expected)

    def test_calculator_square(self):
        """tests the square function"""
        observed = calculator_main.calculator_square(3)
        expected = 9
        self.assertEqual(observed, expected)

    def tearDown(self):
        """This function is run after each test""" 
        pass

if __name__ == "__main__":
    unittest.main()