'''### Square of evens

Write a function which receives a list of ints and returns a new list with the squares of the even numbers. You MUST use `map()`, `filter()`* and lambdas.

Example:

    square_of_evens([1,2,3,4,5,6,7,8,9,10]) == [4, 16, 36, 64, 100]

(*) map and filter are key functions in the functional paradigm. The Well known model MapReduce(http://en.wikipedia.org/wiki/MapReduce) invented by Google uses those function as foundational parts.
'''

def square_of_evens(input1):
    evens = filter(lambda x: x % 2 == 0, input1)
    return map(lambda x: x ** 2, evens)

print square_of_evens([1,2,3,4,5,6,7,8,9,10])