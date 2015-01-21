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

unpack_values([1,2,3])