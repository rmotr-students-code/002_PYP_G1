# 2) Return the line number for a given name or None if the name is not found.

def find_word(input_word):
    with open('names.txt', 'r') as f:
        lines = f.readlines()
    
        word_list = []
    
        for words in lines:
            word_list.append(words.split())
            
        for word in word_list:
            if word[0].lower() == input_word.lower():
                return word[3]
    
print find_word('Eddy')
print find_word('lon')
    