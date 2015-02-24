
# Fibonacci.
# Implement a function that calculates the Fibonacci serie until a given number "n"
# ex: fib(15) with return [0, 1, 1, 2, 3, 5, 8, 13]
# alright there seems to be a recursive way to do this
# def fib_generator(n):
#     a, b = 0,1
#     temp = a 
#     a,b = b, a+b
#     yield temp 
    
def fib(n):
    a, b = 0, 1
    answers = []
    while True:
        temp = a
        if temp > n:
            break
        else:
            answers.append(a)
            a,b = b, a+b
            
    return answers
    

# Capitalize.
# Given a multi word string, return the same string with all first letter as uppercase.
# ex: cap("my name is john") with return "My Name Is John"


#yeah it seems to work maybe we should also have a version which shows the steps that title takes
#ok ill have a shot at that got it
#thanks
# theres more problems below if you want to try those out too
def cap(string):
    word = string.split()
    mylist = []
    
    for entry in word:
        mylist.append(entry.capitalize())
    # might not want to use 'str' as your variable since its a built in method also
    str = " "
    print str.join(mylist)
    
    # return ' '.join([word.capitalize() for word in string.split()])

# Matrix.
# Think about how would you implement a matrix using lists.
# 1. Given a 3x2 matrix, loop over all elements and print them.
# 2. Given a square matrix, print its diagonal.
# gonna see if I can use embedded lists 
def is_square(some_matrix):
    row_length = len(some_matrix)
    
    return all([len(row) == row_length for row in some_matrix])

# nice way of testing your functions:
m1 = [[1,2,3], [2,3,4], [3,4,5]]
m2 = [[1,2,3], [2,3,4]]
assert is_square(m1) == True
assert is_square(m2) == False


def print_diagonal(square):
    diagonal = []
    number_of_rows = sum([1 for row in square])
        
    for i in range(number_of_rows):
        diagonal.append(square[i][i])
    return diagonal

# m1 is defined above
assert print_diagonal(m1) == [1,3,4]
    
def print_elements(some_matrix):
    elements = []
    for entry in some_matrix:
        for single in entry:
            elements.append(single)
    return elements

# m2 is defined above
assert print_elements(m2) == [1,2,3,2,3,4]

def matrix(arg):
    if is_square(arg):
        print_diagonal(arg)
    else:
        print_elements(arg)
        
example_matrix = [[1,2,3],[3,2,1]] #should return the rows
example_square = [[1,2,3],[1,2,3],[1,2,3]] # should return [1,2,3]
example_square2 = [[1,2],[1,2]] # should return [1,2]
assert matrix(example_matrix) == [1,2,3,3,2,1]
assert matrix(example_square) == [1,2,3]
assert matrix(example_square2) == [1,2]
    
# more problems here
# 4.Priority queue. Interface:

#Implement a priority queue with the following interface.

def create_queue():
    new_queue = {}
    return new_queue
    # Creates and returns an empty priorty queue
# new_queue = create_queue()
# assert new_queue == {}
 
def add_element_to_queue(queue, element, priority):
    # Adds the element to the queue with the given priority
    
    if len(queue) == 0:
        queue[element] = priority
    elif element in queue: 
        #update priority level
        queue[element] = priority
    else:
        #add new element with its priority
        queue[element] = priority

def next_element(queue):
    # returns (and removes) the next element in the queue.
    # trying to figure this part out right now
    if len(queue) == 0:
        print("There is no more tasks!")
    else:
        next_priority = min([priority for element, priority in queue.items()])
        
        for element, priority in queue:
            if priority == next_priority:
                next_item = queue.pop(element)
                return next_item

example_queue = create_queue()
assert example_queue == {}
add_element_to_queue(example_queue, "task1", 1)
assert example_queue == {"task1": 1}
add_element_to_queue(example_queue, "task2", 2)
assert example_queue == {"task1": 1, "task2": 2}
# assert next_element(example_queue) == "task1"
# assert next_element(example_queue) == "task2"

"""
# being 1 top priority
queue = create_queue("my_queue")
add_element_to_queue(queue, "clean my house", 5)
add_element_to_queue(queue, "study python", 1)
add_element_to_queue(queue, "visit my girlfriend", 2)
next_element(queue)  # should be "study python"
"""



# 5. Multidict
#You want to make a dictionary that maps keys to more than one value (a so-called "multidict").
#Proposed interface: (you can think your own)

def create_multidict():
    new_dict = {}
    return new_dict

def add_element(some_dict, key, element):
    # need to check if its a new dict
    
    if len(some_dict):
        some_dict[key] = [element]
    elif key in some_dict:
        some_dict[key].append(element)
    # in the case the key doesn't yet exist, we create a new entry
    else:
        some_dict[key] = [element]
    return some_dict

def get_all_elements(some_dict, key):
    return some_dict[key]

example_dict = create_multidict()

add_element(example_dict, 'key1', 'val1')
assert example_dict == {'key1': ['val1'] }
add_element(example_dict, 'key1', 'val2')
assert example_dict == {'key1': ['val1','val2']}
assert get_all_elements(example_dict, 'key1') == ['val1', 'val2']
