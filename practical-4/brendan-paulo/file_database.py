import os

'''
# DATABASE MANAGEMENT SYSTEM
# Build your own database engine, using text files as low level storage method. 
# You are supposed to store one single "table" with information about some topic you decide. 
# Each line of the text file will contain fields separated by some special character
# ("|", ",", ";", etc). The database name, file path, delimiter, and fields order are specified
# at creation time.
# As a user of your database engine, I need to be able to count, insert, update, query and remove
# information from my database.
# The following interface must be respected:


# create the database and insert your first rows.
>>> db = Database(name="students", 
                  filepath="/home/mzugnoni/desktop/students.txt", 
                  delimiter="|",
                  fields=["id", "first_name", "last_name", "country"])
>>> db.insert({"first_name": "Martin", "last_name": "Zugnoni", "country": "Argentina"})
>>> db.insert({"first_name": "Santiago", "last_name": "Basulto", "country": "Argentina"})
 
 
# .count() will return the amount of rows in our database.
>>> db.count()
2
 
 
# .query() will return all rows matching given criteria.
>>> db.query({"country": "Argentina"})
[{"id": 1, "first_name": "Martin", "last_name": "Zugnoni", "country": "Argentina"},
 {"id": 2, "first_name": "Santiago", "last_name": "Basulto", "country": "Argentina"}]
 
 
# .get() will return just one row matching given criteria. If more than one row match the
# criteria, an exception must be raised.
>>> db.get({"fist_name": "Martin"})
{"id": 1, "first_name": "Martin", "last_name": "Zugnoni", "country": "Argentina"}
>>> db.get({"country": "Argentina"})
MultipleObjectsReturned: Your query matched more than one row
 
 
# .update() receibes two dictionaries as argument. The first one is the search criteria,
# and the second one are the fields to be updated. If "multiple" is False (default), only the
# first matched row will be updated.
>>> db.update({"id": 2}, {"first_name": "Santi"}, multiple=False)
>>> db.get({"id": 2})
{"id": 2, "first_name": "Santi", "last_name": "Basulto", "country": "Argentina"}
 
 
# .remove() will delete rows matching the given search criteria. If "multiple" is
# False (default), only the first matched row will be removed.
>>> db.count()
2
>>> db.remove({"id": 1}, multiple=False)
>>> db.count()
1
'''

class Database(object):
    
    def __init__(self, name, filepath, delimiter, fields):
        self.name = name
        self.filepath = filepath
        self.delimiter = delimiter
        self.fields = fields
        self.counter = 0
        i=0     # Write the titles for each column of the database
        with open(self.filepath, 'w') as f:
            for i in range(0,len(self.fields)):
                f.write(self.fields[i] + self.delimiter)
            
            # for i in self.fields:
            #     f.write(self.fields[i] + self.delimiter + '\n')
            
    def insert_db(self, input_dict):
        """Insert a row into database"""
        
        with open(self.filepath, 'a') as f:
            for entry in self.fields:
                f.write(input_dict[entry] + self.delimiter)
            f.write('\n')
                
    def count_db(self):
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                self.counter += 1
            self.counter -= 1
        return self.counter
    
    @staticmethod
    def nomanual(id_, Ranking, First_Name, Last_Name, Country, Prize_Money):
        return {'Id': id_, 
                'Ranking': Ranking, 
                'First_Name': First_Name, 
                'Last_Name': Last_Name, 
                'Country': Country, 
                'Prize_Money': Prize_Money
                }
    

    
    # def query_db(self, input_):
    #     """Search all lines in file for dict key, return line"""
    #     all_data = {}
    #     with open(self.filepath, 'r') as f:
    #         for line in f.readlines():
    #             line_list = line.split("|") # 0, 1, Brendan, Emery, Straya, 90000000
    #             for id_, Ranking, First_Name, Last_Name, Country, Prize_Money in line_list:
    #                 all_data[]
                
                
            #     self.counter += 1
            # self.counter -= 1
            # return self.counter

'''# .query() will return all rows matching given criteria.
>>> db.query({"country": "Argentina"})
[{"id": 1, "first_name": "Martin", "last_name": "Zugnoni", "country": "Argentina"},
 {"id": 2, "first_name": "Santiago", "last_name": "Basulto", "country": "Argentina"}]
'''
    # def update_db(self):
    #     pass

    # def remove_item_db(self):
    #     pass


#fields=["Id", "Ranking", "First_Name", "Last_Name", "Country",  "Prize_Money"]
#print(os.getcwd()) #/home/ubuntu/workspace/practical-4/brendan-paulo/database.txt 
database = Database(name='Players', 
                    filepath='/home/ubuntu/workspace/practical-\
4/brendan-paulo/database.txt', 
                    delimiter='|', 
                    fields=['Id', 'Ranking', 'First_Name', 'Last_Name', 'Country',  'Prize_Money'])


mexican =  {"Id":'0', 
            "Ranking":'1', 
            "First_Name":'Brendan', 
            "Last_Name":'Emery', 
            "Country":'Straya',  
            "Prize_Money":'90000000'
            }
            

mexican1 = database.nomanual('1', '3', 'Paulo', 'Gonzalez', 'USA', '100000000000000')
mexican2 = database.nomanual('2', '4', 'Roger', 'Federer', 'Switzerland', 'Not much')


database.insert_db(mexican)
database.insert_db(mexican1)
database.insert_db(mexican2)

print database.count_db()
print database.counter


