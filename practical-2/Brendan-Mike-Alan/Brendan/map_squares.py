'''
### Map squares

Write a function called squares that receives a list and returns the square of the elements. You MUST use the `map()`* function and lambdas.

Example:
    
    squares([1, 2, 3]) == [1, 4, 9]
'''
def squares(input1):
    return map(lambda x: x ** 2, input1)
print squares([1,2,3])
