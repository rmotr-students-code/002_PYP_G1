class MultipleObjectsReturned(Exception):
    pass

class Database(object):
    
    def __init__(self, name, filepath, delimiter, fields):
        self.name = name
        self.filepath = filepath
        self.delimiter = delimiter
        self.fields = fields
        self.database = []
        self.create_db()    # create the DB txt file  
    
    # db method which creates the db headers in the txt file
    def create_db(self):
        with open(self.filepath, "w") as f:
            for values in range(0,len(self.fields)):
                f.write("{:^8}{:^8}".format(self.fields[values], self.delimiter))
   
   # Insert new records in the db list
    def insert(self, new_record, def_id=1):
        new_entry = {}
        def_id = def_id
        for values in self.database:
            if values['id'] != def_id :
                break
            else:
                def_id += 1
        new_entry['id'] = def_id
        new_entry.update(new_record)
        self.database.append(new_entry)
        
    #update txt file
        with open(self.filepath, 'a') as f:
            f.write("\n{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}".format(new_entry['id'],
            self.delimiter,
            new_entry['make'],self.delimiter,
            new_entry['model'],self.delimiter,
            new_entry['year'],self.delimiter,
            new_entry['cost'],self.delimiter))
    
    #returns the number of records in the DB    
    # works with 1 key:vlaue pair, turns all rows that match
    def count(self):
        return "the database contains {} entries".format(len(self.database))
    
    # A first attempt at creating a query method, requires optimization    
    def query(self, criteria):
        query_result = []
        for entries in self.database:
            for attributes, value in criteria.items():
                if entries[attributes] == value:
                    query_result.append(entries)
        if len(query_result) == 0:
            return ("Database does not contain {}".format(criteria))
        else:
            return query_result
    
    #Query which returns only 1 row, else an error is raised
    def get(self,criteria):
        query_check = self.query(criteria)
        if isinstance(query_check, str):
            return query_check
        elif len(query_check) > 1:
            raise MultipleObjectsReturned("Your query matches more then one row")
        else:
            return query_check
    
    """
    Updates the db with new values.
    if multiple is false, only the first value found is updated. 
    """
    
    def update(self,dic1, dict2, multiple=False):
        pass
    