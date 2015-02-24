class MultipleObjectsReturned(Exception):
    pass

class Database(object):
    def __init__(self, name, filepath, delimiter, fields):
        self.name = name 
        self.filepath = filepath
        self.delimiter = delimiter
        self.fields = fields
        self.database = []
    

    def insert(self, new_info):
        # define the new_id number
        # make that one entry, this entry needs a new id
        # append one entry
        
        new_entry = {}
        new_id = len(self.database) + 1
        
        for key in self.fields:
            if key == "id":
                new_entry[key] = new_id
            
            new_entry[key] = new_info[key]
        
        self.database.append(new_entry)
        
    
    def count(self):
        # return amount of rows in the db
        return len(self.database)
        
        # example format
        # example print(headers)
        # then print rows from db
    
    def query(self, search_criteria):
        # returns all rows given matching criteria.
        query_results = []
        for entry in self.database:
            if search_criteria in entry:
                query_results.append(entry)
        return query_results        
                
    
    def get(self, search_criteria):
        # return one row given criteria, if more than one result is given exception is thrown. 
        query_results = []
        valid_query = False
        for entry in self.database:
            if search_criteria in entry:
                if len(query_results) > 1:
                    valid_query = False
                else:
                    query_results.append(entry)
                    valid_query = True
        if valid_query:
            return query_results
        else:
            raise MultipleObjectsReturned()
    
    def update(self, search_criteria, fields, multiple=False):
        # receives two dicts as args. 1. search criteria. 2. fields to be updated
        # if multiple (default argument )is false, only the first is updated
        # check this later
        key, value = fields.items()
        if multiple:
            for entry in self.database:
                if search_criteria in entry:
                    entry[key] = value
        else:
            for entry in self.database:
                if search_criteria in entry:
                    entry[key] = value
                    break
            
    
    def remove(self, search_criteria, multiple=False):
        # delete entire row given criteria.
        # if multiple (default argument )is false, only the first is deleted
        if multiple: 
            for entry in self.database:
                if search_criteria in entry:
                    self.database.remove(entry)
        else:
            for entry in self.database:
                if search_criteria in entry:
                    self.database.remove(entry)
                    break
    
    # create another method that opens a new file and rewrites over it with the updated db.
    
    # 1. There's alot of repeated of code. So cut down on that.
    # 2. file input() file out()
    # 3. Start looking at speed. timeit module. list comprehensions, other methods
    # 4. testing. write your own  test and see if they work. 