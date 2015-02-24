# #n1
# # Fibonacci.
# # Implement a function that calculates the Fibonacci serie until a given number "n"
# # ex: fib(15) with return [0, 1, 1, 2, 3, 5, 8, 13]

# def fib(n):
#     if n < 2:
#         return 1
#     return fib(n-1) + fib(n-2)   
# pass
    
# #n2
# # Capitalize.
# # Given a multi word string, return the same string with all first letter as uppercase.
# # ex: cap("my name is john") with return "My Name Is John"

# def cap(word):
#     word_capitalized = str(word).title()
#     return word_capitalized
   
# assert cap("hello world") == "Hello world"
   
    
# #n3
# # Matrix.
# # Think about how would you implement a matrix using lists.
# # 1. Given a 3x2 matrix, loop over all elements and print them.
# # 2. Given a square matrix, print its diagonal.

# matrix = [[1,2], #3x2 matrix
#           [3,4],
#           [5,6]]
# for l in matrix:
#     print l
    
# #def play_with_matrix(matrix_input):
    
#     # 3x2 matrix
    
#     #if 
    
#     # square matrix = when elements of the matrix have the same "length as the length of the list"?
#     #123
#     #456
#     #789
#     # returns [1,5,9]
    
#         #print ()

# square_matrix = [['a', 'b', 'c'],  # [0]
#                  ['d', 'e', 'f'],  # [1]
#                  ['g', 'h', 'i']]  # [2]

# square_matrix[0][0]
# square_matrix[1][1]
# square_matrix[2][2]

# def print_diagonal(matrix):
#     for i, elem in enumerate(matrix):
#         print(elem[i][i])
#         #print(elem[i])



def is_square(matrix_input):
    square_list = []
    for itm_number, itm in enumerate(matrix_input):
        # itm_number = 0
        # itm = ['a', 'b', 'c']
        # itm[0] == 'a'
        # 'a'[itm_number]
        if len(itm) == len(matrix_input):
            return square_list.append(itm[itm_number])
        
        else: #our matrix is not square so we print out all elements
            for el in matrix_input:
                for num in el:
                    print(num) #this should work to print out all elems in matrix

# # 4.Priority queue. Interface:

# Implement a priority queue with the following interface.

def create_queue():
#         # Creates and returns an empty priorty queue
    queue = []
    return queue
#         pass
     
def add_element_to_queue(queue, element, priority):
#         # Adds the element to the queue with the given priority
    queue.append(element, priority)
#         pass
     
#     def next_element(queue):
#         # returns (and removes) the next element in the queue.
#         pass

# 5. Multidict
You want to make a dictionary that maps keys to more than one value (a so-called "multidict").
Proposed interface: (you can think your own)

    def create_multidict():
        new_dict = {}
        return new_dict
        pass
    def add_element(target_dict, key, element):
        for key, element in target_dict:
            if key not in 
        pass