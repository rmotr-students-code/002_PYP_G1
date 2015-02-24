#1/23/2015

def create_queue(): # ok
# Creates and returns an empty priorty queue
    queue = []
    return queue

assert create_queue() == [] # ok
     

def add_element_to_queue(queue, element, priority):
     # Ads the element to the queue with the given priority
    queue.append((element, priority))
    pass
     
    def next_element(queue):
        # returns (and removes) the next element in the queue.
        pass



# def is_square(matrix_input):
#     square_list = []
#     for itm_number,itm in enumerate(matrix_input):
#         if len(itm) == len(matrix_input):
#             return True
#         else:
#             return False

# def print_matrix(matrix_input):
#     diagonal_list = []
#     all_items_list = []
#     if is_square(matrix_input) == True:
#         for itm in matrix_input:
#             diagonal_list.append(matrix_input[itm][itm])
#             return diagonal_list
#     else:
#         for itm in matrix_input:
#             all_items_list.append(itm)
#             return all_items_list


# matrix_input = [['a', 'b', 'c'],
#                  ['d', 'e', 'f'],
#                  ['g', 'h', 'i']]

# assert is_square(matrix_input) == True
# print('Looks like it is done')
# print(print_matrix(matrix_input))

# example_matrix = [[1,2,3],[3,2,1]] #should return the rows
# example_square = [[1,2,3],[1,2,3],[1,2,3]] # should return [1,2,3]
# example_square2 = [[1,2],[1,2]] # should return [1,2]
# assert matrix(example_matrix) == [1,2,3,3,2,1]
# assert matrix(example_square) == [1,2,3]
# assert matrix(example_square2) == [1,2]



            
            #print(itm[itm_number])
        
        # else: #our matrix is not square so we print out all elements
        #     for el in matrix_input:
        #         for num in el:
        #             print(num) #this should work to print out all elems in matrix

# #is_square(matrix)  # ['a', 'e', 'i']

# print(is_square([['a', 'b', 'c'],
#                  ['d', 'e', 'f'],
#                  ['g', 'h', 'i']]))

# square_matrix = [['a', 'b', 'c'],
#                  ['d', 'e', 'f'],
#                  ['g', 'h', 'i']] 

# square_matrix = [['a', 'b', 'c'],  # [0]
#                  ['d', 'e', 'f'],  # [1]
#                  ['g', 'h', 'i']]  # [2]
                 
# print(square_matrix[1][1])



# def cap(word):
#     word_capitalized = str(word).title()
#     return word_capitalized
   
# assert cap("hello world") == "Hello World"

# print(cap('yes great'))



#1/20/2015
######################################## 
# def largest_item(input_list):
# # Receives a collection with ints and returns the lartest on
#     # for i in input_list:
#     #     input_list.append(i)
#     #max_item = max(input_list)
#     return(max(input_list))

# print(largest_item([1,2,3]))

    

# def unpack_values(three_element_collection):
# # Receive a collection with 3 elements, unpacks
# # each element in a variable (first, second, third)
# # and prints the three values on string.
# # Prints an error if the collection doesn't have 3 elements.
#     first, second, third = 0, 0, 0 #this might need to be an empty list? []
#     if len(three_element_collection) != 3:
#         return "Does not contain three elements!!!!!"
#     else:
#         first_item = str(three_element_collection[0])
#         second_item = str(three_element_collection[1])
#         third_item = str(three_element_collection[2])

#     print(first_item, second_item, third_item)

# unpack_values([10,11,12])

# def count_evens(collection):
# # Return the number of even ints in the given collection
#     even_numbers = 0
#     for i in collection:
#         if i % 2 == 0:
#             even_numbers += 1
#     return even_numbers
    
# print(count_evens([2,4,5,6,8,9]))