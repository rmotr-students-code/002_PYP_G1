class MultipleObjectsReturned(Exception):
	pass

class Database(object):
	def __init__(self, name, file_path, delimiter, fields):
		self.name = name
		self.file_path = file_path
		self.delimiter = delimiter
		self.fields = fields
		self.header_creator()

	def header_creator(self):
		with open(self.file_path, "w") as f:
			header_str = ''
			for i in range(len(self.fields)):
				header_str += self.fields[i]
				if i == len(self.fields) - 1:
					break
				else:
					header_str += self.delimiter
			header_str += '\n'
			f.write(header_str)
	
	def add_data(self, *args):
		with open(self.file_path, "a") as f:
			new_data_lst = []
			for argument in args:
				for i in range(len(argument.items())):
					if i != len(argument.items())-1:
						new_data_lst.append(argument[self.fields[i]])
						new_data_lst.append(self.delimiter)
					elif i == len(argument.items())-1:
						new_data_lst.append(argument[self.fields[i]])
						new_data_lst.append('\n')
			for lines in new_data_lst:
				f.write(lines)
		self.eliminate_blanks()

	def count(self):
			with open(self.file_path, "r") as f:
				num_lines = sum(1 for line in f) - 1
				print num_lines

	def read_db(self):
			with open(self.file_path, "r") as f:
				print f.read()

	def query(self, search_criteria):
			query_results = []
			with open(self.file_path, "r") as f:
				for line in f:
					(key, value) = search_criteria.items()[0]
					if value in line:
						query_results.append(line)
				if len(query_results) > 0:
					return query_results
				else:
					print "{} not located in the database.".format(search_criteria)
					return query_results

	def get(self, search_criteria):
		query_results = self.query(search_criteria)
		if len(query_results) > 1:
			raise MultipleObjectsReturned("More than one entry was found matching those search parameters.")
		elif len(query_results) == 1:
			return query_results

	def remove(self, search_criteria, multiple = False):
		updated_db = []
		removed_items = 0
		with open(self.file_path, "r") as f:
			for line in f:
				if multiple:
					(key, value) = search_criteria.items()[0]
					if value not in line:
						updated_db.append(line)
					else:
						removed_items +=1
				else:
					(key, value) = search_criteria.items()[0]
					if value not in line:
						updated_db.append(line)
					elif value in line and removed_items == 0:
						updated_db.append(line)
						removed_items += 1
					elif value in line and removed_items > 0:
						removed_items +=1					
					else:
						updated_db.append(line)
				
		if removed_items > 0:
			with open(self.file_path, "w") as f:
				new_data_str = ''
				for i in range(len(updated_db)):
					new_data_str += updated_db[i]
				f.write(new_data_str)

	def update(self, search_criteria,new_entry, Multiple = False):
		self.query(search_criteria)

		if len(self.query(search_criteria)) == 0:
			print "{} not located in the database.".format(search_criteria)

		if len(self.query(search_criteria)) > 0:
			old_db = []
			old_db_dict = dict()
			with open(self.file_path, "r") as f:
				for line in f:
					original_db_values = []
					for word in line.split(','):
						original_db_values.append(word)
					old_db_dict = dict(zip(self.fields,original_db_values))
					old_db.append(old_db_dict)
			old_db.pop(0)
			key_new_entry, value_new_entry = new_entry.items()[0]
			key_search_criteria, value_search_criteria = search_criteria.items()[0]
			for i in range(len(old_db)):
				if old_db[i][key_search_criteria].strip() == value_search_criteria:
					old_db[i][key_new_entry] = value_new_entry
					if Multiple == False:
						break	
			with open(self.file_path, "w") as f:
				self.header_creator()
				for i in range(len(old_db)):
					self.add_data(old_db[i])
				self.eliminate_blanks()

	def eliminate_blanks(self):
		with open(self.file_path,"r") as f:
			lines = f.readlines()
		with open(self.file_path,"w") as f:
			[f.write(line) for line in lines if line.strip()]

