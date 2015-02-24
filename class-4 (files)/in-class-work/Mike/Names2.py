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


def show_line(file_name, number):
    target = None
    with open("{}".format(file_name), 'r') as f:
        for line in f:
            file_num = [value for value in line.strip().split()][3]
            if int(file_num) == number:
                target = line
    if target is not None:
        print(target.strip())
        return "The entry at line {} is: \n{}\n".format(number, target.strip()) 
    else:
        return "The requested entry was not found!"

show_line('names.txt','JAMES')
