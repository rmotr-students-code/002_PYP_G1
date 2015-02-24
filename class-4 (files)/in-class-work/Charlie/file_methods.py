# 1) Count the amount of names starting with a given letter.
def starts_with(file_name, letter):
    count = 0
    with open("{}".format(file_name), 'r') as f:
        for line in f:
            name = [value for value in line.strip().split()][0]
            if name[0] == letter.upper():
                count += 1
    return "{} names start with the letter '{}'.\n".format(count, letter)

# 2) Return the line number for a given name or None if the name is not found.
def show_line(file_name, number):
    target = None
    with open("{}".format(file_name), 'r') as f:
        for line in f:
            file_num = [value for value in line.strip().split()][3]
            if int(file_num) == number:
                target = line
    if target is not None:
        return "The entry at line {} is: \n{}\n".format(number, target.strip()) 
    else:
        return "The requested entry was not found!"

# 3) Return a counter of names starting with each letter from "a" to "z".
def count_names(file_name):
    letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
    name_counts = {}
    
    for letter in letters:
        name_counts[letter] = 0
    
    with open("{}".format(file_name), 'r') as f:
        for line in f:
            name = [value for value in line.strip().split()][0]
            if name[0] in name_counts:
                name_counts[name[0]] += 1
    return "This is the letter dictionary composed of all the names: \n{}\n".format(name_counts)
  
# 4) Sort the file by name in an ascendent way.
def sort_names(file_name, send_data_to_file):
    
    with open("{}".format(file_name), 'r') as f:
        lines = sorted([line for line in f])
    
    # Could reopen the original file and overwrite it here.         
    with open("{}".format(send_data_to_file), "w") as s:
        for line in lines:
            s.write("{}\n".format(line.strip()))
    
    return "Sorting complete. Sorted data has been sent to {}.\n".format(send_data_to_file)
    
# 5) Update all the names containing the string "po" to lowercase.
# Note: This solution only works if name is the only string element per line. 
def update_names(file_name, send_updated_to):
    change_count = 0
    
    with open("{}".format(file_name), 'r+') as f:
        with open("{}".format(send_updated_to), 'w') as u:
            for line in f:
                if "PO" in line:
                    u.write(line.lower())
                    change_count += 1 # Checking to see if the line is being changed.
                else:
                    u.write(line)
    return "{} entries have been changed. Updated data has been sent to {}\n".format(change_count, send_updated_to)    


# Examples

print(starts_with('names1.txt','J')) # returns 100.

print(show_line('names1.txt', 55)) # returns entry at line 55.

print(count_names('names1.txt')) # returns letter count dict.

print(sort_names('names1.txt', 'sort_names.txt')) # sent to a different file to perserve the original. 

print(update_names('names1.txt', 'updated_names.txt')) # ditto.