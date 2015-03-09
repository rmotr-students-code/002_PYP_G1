# importerror? example_db has __init__.py but still getting an error. 
from example_db.example_db import Database, MultipleObjectsReturned
import unittest


class DatabaseTest(unittest.TestCase):

    def setUp(self):
        self.db = Database(name="students",
                           file_path="test_db.txt",
                           delimiter="|",
                           fields=["id", "first_name", "last_name", "country"])
        self.db.insert({"first_name": "Martin", "last_name": "Zugnoni", "country": "Argentina"})
        self.db.insert({"first_name": "Santiago", "last_name": "Basulto", "country": "Argentina"})

    def test_count(self):
        """Should return one more than the current count when inserting another entry"""
        current_count = self.db.count()
        test_info = {"first_name": "Example", "last_name": "User", "country": "USA"}
        self.db.insert(test_info)
        self.assertEqual(current_count+1, self.db.count())

    def test_get(self):
        """Should return MultipleObjectsReturned exception when retrieving more than 1 result"""
        with self.assertRaises(MultipleObjectsReturned):
            self.db.get({"country": "Argentina"})
        self.assertEqual(len(self.db.get({"first_name": "Martin"})), 1)

    def test_remove(self):
        """Should return one less than the current count when deleting an entry."""
        current_count = self.db.count()
        self.db.remove({"id": 1})
        self.assertEqual(self.db.count(), current_count-1)

if __name__ == '__main__':
    # log_file = 'test_logs.txt'
    # with open(log_file, "a") as f:
    #     runner = unittest.TextTestRunner(f)
    #     unittest.main(testRunner=runner, verbosity=2)
    unittest.main()