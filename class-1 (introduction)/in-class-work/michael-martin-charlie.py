#Hi 
# hey everyone
# how about we all take one exercise
# sounds good. then we'll just go through the entire list one by one and discuss if necessary?
# OK I'll take the first one.
#sounds perfect could you also put your name in a comment right after so I know who is doing what

# SEE THIS?

# Here are the exercises I wrote. Just for reference
 
def times(string, times=2):
# Return the `string` str a certain amount of `times`
# times("Hello", 2) == "HelloHello"}
# How to have a default value for times?
# default values can be placed within the function for example times(string, times=2) by default "times" is set to 2
# but if you provided a value for times, then that value is used for "times" instead of default one
# Mike (Done)
    # can assign multiple variables on one line if you want. string, times = str(string), int(times)
    string = str(string)
    times = int(times)
    return string * times
    
print times("Hello",2)
 
 
def unpack_values(three_element_collection):
#Martin Done ... I think
    if len(three_element_collection) != 3:
        print "The collection doesn't have 3 elements"
        return
    # need an else statement here 
    first = three_element_collection[0]
    second = three_element_collection[1]
    third = three_element_collection[2]
    print ("The three elements in the list are {}, {}, {}".format(first, second, third))

    
    # might want to be careful with print statements. In python 3 you need () but in 2.7 you won't need them
# What does 'format(first,second,third) do? Is that the same as using the %s % method?
# format is similar but more used in python 3.3+
# also it's a lot more flexible since you don't have to explicitily state the data type (str, int, float, etc)
    
# Receive a collection with 3 elements, unpacks
# each element in a variable (first, second, third)
# and prints the three values on string.
# Prints an error if the collection doesn't have 3 elements.
 
 
def largest_item(collection):
    # Charlie
    # Receives a collection with ints and returns the largest one
    # return max(collection) # is a similiar function to find the largest value
    
    largest = 0
    for item in collection:
        if item > largest:
            largest = item
    return largest
    
 
def count_evens(collection):
    # Charlie
    # Return the number of even ints in the given collection
    count = 0 
    for value in collection:
        if value % 2 == 0:
            count += 1
    return count