"""Testing Brendan's bank system"""

import unittest
import Brendan_bank_analysis_PG


class Test_Brendan_bank_analysis_PG(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_Account(self):
        
        observed = print(Brendan_bank_analysis_PG.Account(number="123", initial_money=100))
        #print(observed)
        expected = 'Created acct 123 with initial deposit of $100'
        self.assertEqual(print(observed), expected)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
