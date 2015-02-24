'''
### Calculator based on functions

Define a couple of mathematical operation functions. For example:

    sum(1, 5, 6)      # Should return 12
    sum(1, 3)         # Should return 4
    subtract(5, 2)    # Should return 3
    subtract(5, 2, 1) # Should return 2

Create a calculator that can take a function operation and a list of arguments to process:

    calculator(sum, 1, 5, 6)   # Should return 12
    #           ^ This is our previously defined `sum` function
    calculator(sum, 1, 3)      # Should return 4
    calculator(subtract, 5, 2) # Should return 3
'''

def sum_(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(*args):
    """Multiply the first value by 2 because it will subtract the value once in 
    the first iteration"""
    total = 2 * args[0]
    for num in args:
        total -= num
    return total
    
def calculator(function, *args):
    return function(*args)

# print calculator(sum_, 1,2,3)