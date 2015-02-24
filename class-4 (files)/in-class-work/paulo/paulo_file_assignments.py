#Given the "names.txt" file, write separate programs for each of the following points:
#1) Count the amount of names starting with a given letter.
#2) Return the line number for a given name or None if the name is not found.
#3) Return a counter of names starting with each letter from "a" to "z".
#4) Sort the file by name in an ascendent way.
#5) Update all the names containing the string "po" to lowercase.

# with open('names.txt', 'r') as f:
#     #print(f.read()) #ok
    
#1

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def Count_Names(file_input, letter):
    
    with open(file_input, 'r') as f:
        
        #data_list = []
        # for line in f.readlines():# split():
        #     data_list.append(line.split())

        data_list = [line.split() for line in f.readlines()]

        # name_list = []
        # for name in data_list:
        #     name_list.append(name[0])
        
        name_list = [name[0] for name in data_list] #LC

        # count_list = []
        # for first_letter in name_list:
        #     if first_letter[0] == letter:
        #         count_list.append(first_letter)
        
        count_list = [first_letter for first_letter in name_list if first_letter[0] == letter]
        
        return len(count_list)
        
#print(Count_Names('names.txt', 'A')) # OK

#2) Return the line number for a given name or None if the name is not found.

def return_line_number(file_input, input_name):
    
    with open(file_input, 'r') as f:
        
        #data_list = []
        # for line in f.readlines():# split():
        #     data_list.append(line.split())

        data_list = [line.split() for line in f.readlines()]
        name_list = [name[0] for name in data_list]
        
        matches= []
        for line_number, first_name in enumerate(name_list):
            if str(first_name).lower() == str(input_name).lower():
                matches.append(line_number)
        
        # matches = [line_number, first_name in enumerate(name_list) if str(first_name).lower() == str(input_name).lower()]
        
        return matches
            
#print(return_line_number('names.txt', "PAUL")) # OK

#3) Return a counter of names starting with each letter from "a" to "z".

