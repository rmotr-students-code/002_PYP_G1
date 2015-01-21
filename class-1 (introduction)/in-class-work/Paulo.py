def largest_item(input_list):
# Receives a collection with ints and returns the lartest on
    # for i in input_list:
    #     input_list.append(i)
    #max_item = max(input_list)
    return(max(input_list))

print(largest_item([1,2,3]))

    

def unpack_values(three_element_collection):
# Receive a collection with 3 elements, unpacks
# each element in a variable (first, second, third)
# and prints the three values on string.
# Prints an error if the collection doesn't have 3 elements.
    first, second, third = 0, 0, 0 #this might need to be an empty list? []
    if len(three_element_collection) != 3:
        return "Does not contain three elements!!!!!"
    else:
        first_item = str(three_element_collection[0])
        second_item = str(three_element_collection[1])
        third_item = str(three_element_collection[2])

    print(first_item, second_item, third_item)

unpack_values([10,11,12])

def count_evens(collection):
# Return the number of even ints in the given collection
    even_numbers = 0
    for i in collection:
        if i % 2 == 0:
            even_numbers += 1
    return even_numbers
    
print(count_evens([2,4,5,6,8,9]))