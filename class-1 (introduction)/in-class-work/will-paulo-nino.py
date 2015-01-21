# Here are the exercises I wrote. Just for reference



def times(string, times=2):
# Return the `string` str a certain amount of `times`
# times("Hello", 2) == "HelloHello"}
# How to have a default value for times? 
    return string * times



#works 
def unpack_values(three_element_collection):
# Receive a collection with 3 elements, unpacks
# each element in a variable (first, second, third)
# and prints the three values on string.
# Prints an error if the collection doesn't have 3 elements.
    if len(three_element_collection) != 3:
        print("Does not contain three elements!!!!!")
    else:# need an else statement here
        first_item = str(three_element_collection[0])
        second_item = str(three_element_collection[1])
        third_item = str(three_element_collection[2])

    print(first_item, second_item, third_item)

#Try running it in another file
 
 
#works
def largest_item(input_list): 
# Receives a collection with ints and returns the largest on
    return max(input_list)

print(largest_item([1,2,3]))
    

#works!
def count_evens(collection):
# Return the number of even ints in the given collection
    even_numbers = 0
    for i in collection:
        if i % 2 == 0:
            even_numbers += 1
    return even_numbers