# Function with only no-named arguments. 

def introduction(name, place, mood):
    return "Hello {} from {}. Currently, you feel {}".format(name, place, mood)

assert introduction("Chuck", "Chicago", "cold") == "Hello Chuck from Chicago. Currently, you feel cold"

# Function with only named arguments.

def named_example(arg1, arg2):
    return "{} plus {} should equal {}".format(arg1, arg2, arg1+arg2)

assert named_example(arg1=1,arg2=2) == "1 plus 2 should equal 3"

# Function with both named and no-named arguments.

def both_kinds(arg1, arg2, arg3):
    return "Arg1: {}. Arg2: {} Arg3 should be changed to: {}".format(arg1, arg2, arg3)
    
assert both_kinds("This is argument 1", "This is argument 2", arg3="Changing argument 3") == "Arg1: This is argument 1. Arg2: This is argument 2 Arg3 should be changed to: Changing argument 3"

# Function using special *args and **kwargs arguments.
 
def special_arg(*args, **kwargs):
    all_args = [i for i in args]
    all_kwargs = [var_value*2 for var_name,var_value in kwargs.items()]
    
    return "Args: {} Kwargs: {}".format(all_args, all_kwargs)

assert special_arg("hello", "hi", 2, 3, name1='Charlie', name2='Joey') == "Args: ['hello', 'hi', 2, 3] Kwargs: ['JoeyJoey', 'CharlieCharlie']"

# Function using some optional arguments.

def your_day(mood="happy", weather="bright and sunny"):
    return "You're feeling {} because the weather is {}!".format(mood, weather)
    
assert your_day() == "You're feeling happy because the weather is bright and sunny!"

# Function using the "return" keyword. Assing the result of the function to a variable

def some_function():
    return "This is the result"

the_result = some_function()
assert the_result == "This is the result"

# Function that receives another function as argument and executes it.
 
def first(default_sentence="This is the first sentence"):
    return default_sentence

def argument_printer(some_function, some_argument):
    return some_function(some_argument)
    
assert argument_printer(first, "I don't like the default") == "I don't like the default"
    
 
# Assign an anonymous function (lambda) to a variable and execute it.
 
squared = lambda a: a**2 
numbers = 5

def square_nums(squared, nums):
    return squared(nums)

assert square_nums(squared, numbers) == 25

# Anonymous function (lambda) with more than one argument.

product = lambda a,b: a*b
num1, num2 = 2, 5

def test(operation, var1, var2):
    return operation(var1, var2)
    
assert test(product, num1, num2) == 10