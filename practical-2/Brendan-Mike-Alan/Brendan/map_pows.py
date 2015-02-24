'''### Map pows

Modify your previous function to receive one more argument "power" which should be optional (default to 2) that will be the power to raise each element on the list. Again, you MUST use `map()`* and lambdas.

    exponentiation([1, 2, 3], power=3) == [1, 8, 27]
'''

def exponentiation(input1, power=3):
    return map(lambda x: x ** power, input1)

print exponentiation([1,2,3,4,5], 2)
