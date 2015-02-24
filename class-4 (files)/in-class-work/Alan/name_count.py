

def count_starting_with(letter):
    counter = 0
    with open('names.txt', 'r') as f:
        for line in f:
            if line.startswith(letter):
                counter +=1
    return counter
    
print count_starting_with('A')
        