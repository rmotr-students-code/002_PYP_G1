# 3) Return a counter of names starting with each letter from "a" to "z".
import string

def count_names():
    with open('names.txt', 'r') as f:
        lines = f.readlines()
    
        name_list = []
        my_dict = populate_dict()
        
        for line in lines:
            name_list.append(line.split()[0])
    
        for name in name_list:
            assert name[0].isalpha()
            my_dict[name[0].lower()] += 1
        
        return my_dict
        
def populate_dict():
    dict_ = {}
    for letter in string.ascii_lowercase:
        dict_[letter] = 0
    return dict_

print count_names()