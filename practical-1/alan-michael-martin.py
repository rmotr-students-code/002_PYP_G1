# Fibonacci.
# Implement a function that calculates the Fibonacci serie until a given number "n"
# ex: fib(15) with return [0, 1, 1, 2, 3, 5, 8, 13]

def fib(n):
    if n == 1:
        return 1
    else:
        return n + fib(n - 1)
    

#Mike
# Capitalize.  - have you resolved you issue? No .. ok im looking at it 
#well it sort of works, you just have to stick it all back together into a sentence

# Given a multi word string, return the same string with all first letter as uppercase.
# ex: cap("my name is john") with return "My Name Is John"

# " ".join(w[0].upper() + w[1:])   == > "world" > "World"
# [] + "World" => ['W', 'o', 'r', 'l', 'd']
# "" + "World" => "World"
def cap(word):
    z = []
    y = []
    for w in word.split():
        z = w[0].upper() + w[1:]
        y.append(z)
        x = " ".join(y)
    return x


    
    

#Marty    
# Matrix.
# Think about how would you implement a matrix using lists.
# 1. Given a 3x2 matrix, loop over all elements and print them.
# 2. Given a square matrix, print its diagonal.
grid = [[ 1, 0, 6],
        [2, 8, 9],
        [6, 5, 8]]
        
def print_elements(matrix):
    for elements in matrix:
        return elements
 
    
def print_diagnal(matrix):
    i = 0
    diagnal = []
    for elements in matrix: #so the 1st iteration will get you the first list
        diagnal.append(elements[i]) 
        i += 1     
    return diagnal   
    
    
def is_square(matrix):
    lenght = [len(matrix)]
    for elements in matrix:
        width = []
        if elements not in width:
            width.append(len(elements))
        else:
            pass
    if lenght == width:
        return True
    else:
        return False
        
        
    #try making the position of the element a variable, setting it to a number 
    #initially. Then as you go through the loop, add to that number . 
    #yes you can access elements inside the lists within the list, using the index
    #so like.. if list = [[1,2],[3,4]]
    #the first for loop takes you to object [1,2]
    #so you can get the 2nd item in that object by object[1]
    #if that makes sense ... yeah , that works, 
#I thought of a way to write it but i can wait till you finish first - Alan ... thanks we can compare :) 
###Having a hard time figuring out how I would get to the 2nd element of the second line and the 3rd from the 3rd line
#yup!

# 4.Priority queue. Interface:

# Implement a priority queue with the following interface.

def create_queue(name):
    name = []
    return name
    # Creates and returns an empty priorty queue

'a', 3
'g', 0
'd', 1
'z', 1

#[('g', 0), ('z', 1), ('d', 1), ('a', 3)]

# data structure looks like queue = [(item, priority), (item2, priority)] 
def add_element_to_queue(queue, element, priority):
    # [ ('a', 3) ]
    position = 0
    for item in queue:
        current_item_priority = item[1]
        if current_item_priority < priority:
            pass
        elif current_item_priority >= priority:
            queue.insert(position, (element, priority))
        position += 1

    # this point
    # position == 0
    queue.insert(position, (element, priority))

 
def next_element(queue):
    # returns (and removes) the next element in the queue.
    pass

# being 1 top priority
queue = create_queue("my_queue")
add_element_to_queue(queue, "clean my house", 5)
add_element_to_queue(queue, "study python", 1)
add_element_to_queue(queue, "visit my girlfriend", 2)
next_element(queue)  # should be "study python"

# ////////////////////////////////////////Marty's priority queue implementation

def create_queue(name):
    name = []
    return name
    # Create the queue

# data structure looks like queue = [(item, priority), (item2, priority)] 
def add_element_to_queue(queue, element, priority):
    #check if the queue is emplty , else priority is the 1st element in the queue
    if len(queue) == 0:
        queue.insert(0, (element, priority))
    else: 
        queue_priority = queue[0][1]
        # check if new items would fit in queue position [0]
        if priority <= queue_priority:
            queue.insert(0,(element, priority))
        # else, loop through the queue to determine where to insert the new item    
        else:
            element_added = False
            lookup = -1            
            while element_added == False:
                try :
                    lookup += 1
                    if priority <= queue[lookup][1]:
                        queue.insert(lookup, (element, priority))
                        element_added = True                    
                    else:
                        pass
                except IndexError:
                    queue.append((element, priority))
                    element_added = True  
    return queue    

def next_element(queue):
    return queue[0]

queue = create_queue("my_queue")
add_element_to_queue(queue, "a", 2)
add_element_to_queue(queue, "b", 6)
add_element_to_queue(queue, "c", 6)
add_element_to_queue(queue, "d", 1)
add_element_to_queue(queue, "e", 2)
add_element_to_queue(queue, "e", 5)
print next_element(queue) 

# ////////////////////////////////////////////////////////////////////////////


# 5. Multidict
You want to make a dictionary that maps keys to more than one value (a so-called "multidict").
Proposed interface: (you can think your own)

    def create_multidict():
        pass
    def add_element(dict, key, element):
        pass