from file_database import *
import unittest


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database(name='Players',
                                 filepath='C:\Users\Brendan\Google Drive\Programming\Python\Python Course 2\Practical 4\database.txt',
                                 delimiter='|',
                                 fields=['Id', 'Ranking', 'First_Name',
                                         'Last_Name',
                                         'Country', 'Prize_Money'])
        self.count = 0

        # Should I insert the lines to use for tests here or in self.test_insert_
        # db?

        self.database.insert_db({'Ranking': '1',
                                 'First_Name': 'Roger',
                                 'Last_Name': 'Federer',
                                 'Country': 'Straya',
                                 'Prize_Money': '$1000000'})

        self.database.insert_db({"Ranking": '2',
                                 "First_Name": 'Roger',
                                 "Last_Name": 'Emery',
                                 "Country": 'Straya',
                                 "Prize_Money": '90000000'})

        self.database.insert_db({"Ranking": '4',
                                 "First_Name": 'DA',
                                 "Last_Name": 'GAawG',
                                 "Country": 'Straya',
                                 "Prize_Money": '1'})

        self.line_1 = {'Ranking': '1',
                       'First_Name': 'Roger',
                       'Last_Name': 'Federer',
                       'Prize_Money': '1000000',
                       'Country': 'Straya',
                       'Id': '1'}

        self.line_2 = {"Ranking": '2',
                       "First_Name": 'Roger',
                       "Last_Name": 'Emery',
                       "Country": 'Straya',
                       "Prize_Money": '90000000',
                       "Id": '2'}

        self.line_3 = {"Ranking": '4',
                       "First_Name": 'DA',
                       "Last_Name": 'GAawG',
                       "Country": 'Straya',
                       "Prize_Money": '1',
                       "Id": '3'}

    def test_insert_db(self):
        """Should be able to find line when get_db searches for the unique Id"""
        self.database.insert_db({"Ranking": '5',
                                 "First_Name": 'John',
                                 "Last_Name": 'Smith',
                                 "Country": 'US',
                                 "Prize_Money": '12'})
        self.assertEquals(self.database.get_db({'Id':
                                                    str(self.database.count_db()
                                                    )})
                          , [{"Ranking": '5',
                              "First_Name": 'John',
                              "Last_Name": 'Smith',
                              "Country": 'US',
                              "Prize_Money": '12',
                              'Id': str(self.database.count_db())}])

    def test_query_db(self):
        """Should return a list of matching lines as dicts when query_db
        searches for a key/value pair present in the database"""
        self.assertEquals(self.database.query_db(
            {'Id': '1'}), [self.line_1])
        self.assertEquals(self.database.query_db(
            {'First_Name': 'Roger'}), [self.line_1, self.line_2])
        self.assertEquals(self.database.query_db(
            {'Country': 'Straya'}), [self.line_1, self.line_2, self.line_3])
        self.assertEquals(self.database.query_db(
            {'Id': 'Doesn\'t exist'}), [])

    def test_check_dict_no_match(self):
        """Should raise an error when the search value isn't found in the input
        dictionary"""
        with self.assertRaises(KeyNotInDict):
            Database.check_dict_for_search_value(
                {'a': '1', 'b': '2', 'c': '2'}, {'d': 4})

    def test_check_dict_for_search_value(self):
        """Should return true when search value is in input dictionary"""
        self.assertTrue(Database.check_dict_for_search_value(
            {'a': '1', 'b': '2', 'c': '3'}, {'a': '1'}), True)

    def test_remake_dict(self):
        """Should return a dict of values in line when the line is input"""
        self.assertEquals(self.database.remake_dict(' 1 2 B E S 10 '),
                          {'Id': '1',
                           'Ranking': '2',
                           'First_Name': 'B',
                           'Last_Name': 'E',
                           'Country': 'S',
                           'Prize_Money': '10'}
        )

    def test_get_db(self):
        """Should return the line as a dict when the line contains the search
        criteria"""
        self.assertEquals(self.database.get_db({'Last_Name': 'Federer'}),
                          [self.line_1])

    def test_get_db_no_match(self):
        """Should raise an error when search criteria doesn't matches more than
         one line"""
        with self.assertRaises(MultipleObjectsReturned):
            self.database.get_db({'Country': 'Straya'})

    def test_update_db_no_multiples(self):
        """query_db should return the lines that were not updated as they were
        multiples (but still contain the search criteria) when searching for the
        original line"""
        self.database.update_db({'Country': 'Straya'},
                                {'Country': 'NotStraya'},
                                multiple=False)
        self.assertEquals(self.database.query_db({'Country': 'Straya'}),
                          [self.line_2, self.line_3])

    def test_update_db_with_multiples(self):
        """query_db should return an empty list when searching for the original,
            un-updated line"""
        self.database.update_db({'Country': 'Straya'},
                                {'Country': 'NotStraya'},
                                multiple=True)
        self.assertEquals(self.database.query_db({'Country': 'Straya'}), [])

if __name__ == '__main__':
    unittest.main()