"""### Calculator dict

Similar to our previous exercise, but the interface of the calculator is different:

    calculator('sum', 1, 5, 6)   # Should return 12
    #           ^ This is a String
    calculator('sum', 1, 3)      # Should return 4
    calculator('subtract', 5, 2) # Should return 3

It now accepts a string as the operation name.

IMPORTANT: You can't use if statements. You have to use a dictionary.
"""
from calculator import sum_, subtract
my_dict = {'sum' : sum_, 'subtract' : subtract}

def calculator_(function, *args):
    return my_dict[function](*args)

print calculator_('subtract', 2,1,3)