# 1) Count the amount of names starting with a given letter.

def count_word(letter):
    with open('names.txt', 'r') as f:
        lines = f.readlines()
    
        words = []
        count = 0
    
        for line in lines:
            words.append(line.split()[0])
        
        for word in words:
            if word[0] == letter:
                count += 1
        return count

print count_word('A')