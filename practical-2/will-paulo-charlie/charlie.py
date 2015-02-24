# Assignments


### *mutability

mutable_list = [1,2,3]
immutable_list = [1,2,3]

def mutable_append(mutable_list, item):
    mutable_list.append(item)    
    return mutable_list
    
assert mutable_append(mutable_list, 'a') == [1,2,3,'a']

def immutable_append(immutable_list, item):
    new_list = [value for value in immutable_list]
    new_list.append(item)
    return new_list

assert immutable_append(immutable_list, 'a') == [1,2,3,'a']
assert immutable_list == [1,2,3] # make sure the immutable list was not changed

### Average

#Write a function that can either receive a list or different integer arguemnts and computes the Average:
def find_average(numbers):
    list_of_numbers = [int(n) for n in numbers]
    total = sum(list_of_numbers)
    number_of_values = len(list_of_numbers)
    return float(total) / float(number_of_values)

def average(*nums):
    if len(nums) == 1:
        return find_average(nums[0])
    else:
        return find_average(nums)

assert average(1,5,3,2) == 2.75
assert average([1,5,3,2]) == 2.75

### Pack

# Write a function that receives an arbitrary amount of params and build a list with them.

def build_list(*params):
    new_list = [element for element in params]
    return new_list

assert build_list(1, 5, "hello") == [1, 5, "hello"]

### Map squares

# Write a function called squares that receives a list and returns the square 
# of the elements. You MUST use the `map()`* function and lambdas.

def squares(numbers):
    return map(lambda x: x**2, numbers)

assert squares([1, 2, 3]) == [1, 4, 9]

### Map pows

# Modify your previous function to receive one more argument "power" which should be optional (default to 2) 
# that will be the power to raise each element on the list. Again, you MUST use `map()`* and lambdas.

def exponentiation(numbers, power=2):
    return map(lambda x: x**power, numbers)

assert exponentiation([1, 2, 3], power=3) == [1, 8, 27]

### Square of evens
# Write a function which receives a list of ints and returns a new list with the squares of the even numbers. 
# You MUST use `map()`, `filter()`* and lambdas.

def square_of_evens(numbers):
    squared_nums = squares(numbers)
    return filter(lambda y: y%2==0, squared_nums)
    
assert square_of_evens([1,2,3,4,5,6,7,8,9,10]) == [4, 16, 36, 64, 100]

### Min max
# Given a list of integers return the largest and the smallest values.

def minmax(numbers):
    return "Min: {min(numbers)} Max: {max(numbers)}"

### Calculator based on functions

# Define a couple of mathematical operation functions. 

def find_sum(*numbers):
    return sum([int(i) for i in numbers])

def subtract(*numbers):
    # all_numbers = [int(i) for i in numbers]
    # total = 0
    # for index, value in all_numbers:
    #     if index == 0:
    #         total = value
    #     else:
    #         total -= value
    # return total        
    
    subtractor = lambda a,b: a-b
    return reduce(subtractor, [int(i) for i in numbers])

assert find_sum(1, 5, 6) == 12
assert find_sum(1, 3) == 4        
assert subtract(5, 2) == 3   
assert subtract(5, 2, 1) == 2
# Create a calculator that can take a function operation and a list of arguments to process:

def calculator(operation, *numbers):
    return operation(*numbers)

assert calculator(find_sum, 1, 5, 6) == 12
assert calculator(find_sum, 1, 3) == 4
assert calculator(subtract, 5, 2) == 3

### Calculator dict

# Similar to our previous exercise, but the interface of the calculator is different:
# IMPORTANT: You can't use if statements. You have to use a dictionary.

def calculator1(operation, *numbers):
    operations = {
            'add': find_sum(*numbers),
            'subtract': subtract(*numbers)
    }
    
    return operations[operation]


assert calculator1('add', 1, 3) == 4
assert calculator1('subtract', 5, 2) == 3