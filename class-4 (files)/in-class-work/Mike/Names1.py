#1) Count the amount of names starting with a given letter.


with open('names.txt', 'r') as f:
    count = 0
    for name in f:
        if name[0] == 'J':
            count += 1
    print count


    