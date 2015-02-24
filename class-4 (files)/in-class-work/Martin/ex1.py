#with open('names.txt', 'r') as f:
#    for line in f:
#       print(name, num1, num2, file_num = [value for value in line.strip().split()])

#1) Count the amount of names starting with a given letter.
def name_count(file_name, letter):
    count = 0
    with open(file_name, 'r') as names:
        for lines in names:
            if lines.startswith(letter):
                count += 1
    return count
    
#print name_count('names.txt','M')
    
#2) Return the line number for a given name or None if the name is not found.

def name_locator(file_name, name):
    with open(file_name, 'r') as names:
        result = None
        for lines in names:
            if lines.split()[0] == name:
                result = lines.split()[3]
            else:
                pass
            
        if result == None:
            return "Name not found"
        else:
            return "{} is located at position {}".format(name, result)
            
#print name_locator("names.txt", name="JOHN")

#3) Return a counter of names starting with each letter from "a" to "z".              
def first_letter_count(file_name):
    letter_dict = {}
    with open(file_name, 'r') as names:
        for lines in names:
            if lines.split()[0][0] in letter_dict.keys():
                letter_dict[lines.split()[0][0]] += 1
            else:
                letter_dict[lines.split()[0][0]] = 1
        return letter_dict
    
#print first_letter_count("names.txt")    

#4) Sort the file by name in an ascendent way.
def ascend_sort(file_name):
    
    pass
    

#5) Update all the names containing the string "po" to lowercase.