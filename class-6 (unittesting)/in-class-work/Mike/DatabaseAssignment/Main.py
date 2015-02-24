from Database.MikeDB import *

database1 = Database('DB1','text1.txt',',',['id','first_name', 'last_name'])
entry1 = {'id': '1', 'first_name': 'Mike', 'last_name': 'Azar'}
entry2 = {'id': '2', 'first_name': 'John', 'last_name': 'Smith'}
entry3 = {'id': '3', 'first_name': 'Mike', 'last_name': 'Twain'}
entry4 = {'id': '4', 'first_name': 'Tim', 'last_name': 'Valbuena'}
entry5 = {'id': '5', 'first_name': 'Joey', 'last_name': 'Mustafa'}
entry6 = {'id': '6', 'first_name': 'Tom', 'last_name': 'Jerry'}

s = {'id': '2'}
r = {'last_name': 'HMAR'}

s1 = {'last_name': 'HMAR'}
r1 = {'id': '9'}


database1.add_data(entry1,entry2,entry3,entry4,entry5,entry6)
database1.read_db()
