import re


class MultipleObjectsReturned(Exception):
    pass


class KeyNotInDict(Exception):
    pass


class Database(object):
    def __init__(self, name, filepath, delimiter, fields):
        self.name = name
        self.filepath = filepath
        self.delimiter = delimiter
        self.fields = fields
        self.id_count = 1
        self.space = ' '

        self.setup_column_titles()

    def setup_column_titles(self):
        # Set up the titles in the database based on the user's "Fields" input
        with open(self.filepath, 'w') as f:
            for value in range(0, len(self.fields)):
                f.write(2 * self.space + self.fields[value] + 2 * self.space +
                        self.delimiter)
            f.write('\n')

    def insert_db(self, input_dict):
        """Write the values to the file"""
        # Insert ID value into line
        with open(self.filepath, 'a') as f:
            if self.id_count < 10:
                f.write(2 * self.space + str(self.id_count) + 3 * self.space
                        + self.delimiter)
            else:
                f.write(2 * self.space + str(self.id_count) + 2 * self.space
                        + self.delimiter)

            for value in self.fields[1:]:
                # Add 4 to count the whitespaces around each title value
                if (len(value) + 4) > len(input_dict[value]):
                    implement_space = len(value) + 4 - len(input_dict[value])
                else:
                    implement_space = 0
                f.write(input_dict[value] + implement_space * self.space +
                        self.delimiter)
            self.id_count += 1
            f.write('\n')

    def count_db(self):
        return self.id_count - 1

    def query_db(self, search_criteria):
        """Check to see if search criteria is in any line in the database"""
        with open(self.filepath, 'r') as f:
            lines = f.readlines()
            list_return = []

            # Skip the first line of the database so it doesn't search titles
            for line in lines[1:]:
                line_dict = self.remake_dict(line)
                # Check if function returns True ie. There is a match
                if Database.check_dict_for_search_value(
                        searchable_dict=line_dict,
                        search_criteria=search_criteria):
                    list_return.append(line_dict)
            return list_return

    @staticmethod
    def check_dict_for_search_value(searchable_dict, search_criteria):
        for key, value in search_criteria.items():
            try:
                if searchable_dict[key] == value:
                    return True
            except:
                # raise NotImplementedError
                raise KeyNotInDict('Key is not in dict. Check case')

    def remake_dict(self, line):
        """Make a dictionary from a line in the database"""
        new_dict = {}
        i = 0
        ret_list = re.split(r'\W*', line)
        for val in ret_list[1:-1]:
            new_dict[self.fields[i]] = val
            i += 1
        return new_dict

    def get_db(self, search_criteria):
        """Return row if only one row matches the search criteria"""
        search_values = self.query_db(search_criteria)
        if isinstance(search_values, list) and len(search_values) > 1:
            raise MultipleObjectsReturned('Your query matched more than one row'
            )
        else:
            return self.query_db(search_criteria)

    def update_db(self, search_criteria, update_criteria, multiple=False):

        line_list = []
        check_again = True
        with open('database.txt', 'r+') as f:
            # Read each line and add it/updated version as a dictionary to a
            # list
            for line in f.readlines()[1:]:
                line_dict = self.remake_dict(line)
                if Database.check_dict_for_search_value(line_dict,
                                                        search_criteria) \
                        and check_again is True:
                    for key, value in update_criteria.items():
                        line_dict[key] = value
                    line_list.append(line_dict)
                    check_again = multiple
                else:
                    line_list.append(line_dict)
            # Clear the file and rewrite the list of dictionaries line by line
            self.id_count = 1
            f.seek(0, 0)
            f.truncate()
            self.setup_column_titles()
            for dict_ in line_list:
                self.insert_db(dict_)

    def remove_db(self, searchable_criteria, multiple):
        line_list = []
        check_again = True
        with open(self.filepath, 'r+') as f:
            # Check if any row matches the search value
            for line in f.readlines()[1:]:
                line_dict = self.remake_dict(line)
                if Database.check_dict_for_search_value(line_dict,
                                                        searchable_criteria) \
                        and check_again is True:
                    check_again = multiple
                else:
                    line_list.append(line_dict)

            self.id_count = 1
            f.seek(0, 0)
            f.truncate()
            self.setup_column_titles()
            for dict_ in line_list:
                self.insert_db(dict_)


def main():
    database = Database(name='Players',
                        filepath='C:\Users\Brendan\Google Drive\Programming\Python\Python Course 2\Practical 4\database.txt',
                        delimiter='|',
                        fields=['Id', 'Ranking', 'First_Name', 'Last_Name',
                                'Country', 'Prize_Money'])

    database.insert_db({'Id': '1',
                        'Ranking': '1',
                        'First_Name': 'Roger',
                        'Last_Name': 'Federer',
                        'Country': 'Switzerland',
                        'Prize_Money': '$1000000'})

    database.insert_db({"Id": '0',
                        "Ranking": '2',
                        "First_Name": 'Roger',
                        "Last_Name": 'Emery',
                        "Country": 'Straya',
                        "Prize_Money": '90000000'
    })

    database.insert_db({"Id": '0',
                        "Ranking": '4',
                        "First_Name": 'DA',
                        "Last_Name": 'GAawG',
                        "Country": 'Straya',
                        "Prize_Money": '1'
    })

    database.count_db()
    print database.query_db({'Country': 'Straya'})
    database.get_db({'First_Name': 'DA'})
    database.update_db({'Id': '3'}, {'First_Name': 'Santi'}, True) #NOT WORKING FOR ID
    # database.remove_db({'Country': 'Switzerland'}, True)

main()