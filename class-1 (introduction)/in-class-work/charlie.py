# numbers = [1, 2.5]
# print("{} is an integer".format(numbers[0]))
# print("{} is a float".format(numbers[1]))

# basic_functions = 5/2 # example of division


# n = ["This", "is", "a", "list"]
# for word in n:
#     print(word)

# my_info = {
#         "name": "Charlie",
#         "age": 22,
#         "location": "Los Angeles"
#         }

# print("My name is {} and I am {} years old. Currently, I live in {}".format(my_info["name"],my_info["age"],my_info["location"]))

# tuple_example = (1,2)

# def basic_greeting(name):
#     print("Hey {}, it's nice to meet you!".format(name))

# your_name = input("What is your name?").capitalize()
# basic_greeting(your_name)

# Classwork 1/20

def times(string, times=2):
    
    return string*times
 
 
def unpack_values(three_element_collection):

    if three_element_collection.lenght == 3:
        first = three_element_collection[0]
        second = three_element_collection[1]
        third = three_element_collection[2]
        print("The three items are {}, {}, {}".format(first, second, third))
    else:
        "There are not 3 elements in that list!"
 
def largest_item(collection):
    # can use max(collection)
    largest = 0
    for item in collection:
        if item > largest:
            largest = item
    return largest
 
def count_evens(collection):
    count = 0
    for item in collection:
        if item % 2 == 0:
            count += 1
    return count 