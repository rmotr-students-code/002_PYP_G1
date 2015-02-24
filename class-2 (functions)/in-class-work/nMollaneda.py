### PLAYING WITH FUNCTIONS

## function with only no-named arguments. 
   #(try sending arguments i n diferent order when executing)
def some_function(name, number):
    print(name)
    print(number * number)
    
some_function("somethingSomething", 3)

## function with only named arguments.
   #(try sending arguments in diferent order when executing)
some_function(number = 5, name = "thisThat")

## function with both named and no-named arguments.
   #(named arguments must be on the right part of the argument list)
some_function("howAboutThis", number = 6)

## function using special *args and **kwargs arguments.
def infinite_arguments(*args):
    for args in args:
        print(args)

infinite_arguments(1,2,3,4,4,5,6,6,7,7,8,89,9)
 
## function using some optional arguments.
   #(try executing the funcion both sending and not sending the optional parameter)
def optional_arguments(name, number, country = "Philippines"):
    print(name)
    print(number * number)
    print(country)
    
optional_arguments("ohNo", 42)

## function using the "return" keywork. Assing the result of the function to a variable
def return_function(name):
    return name

give_me_something = return_function("YourName")
print(give_me_something)
 
## function that receives another function as argument and executes it.
def func_in_func(some_other_function):
    print(some_other_function)

func_in_func(give_me_something)
 
## Assign an anonymous function (lambda) to a variable and execute it.
multiply_lambda = lambda num_one, num_two : num_one * num_two
print(multiply_lambda(2,4))
 
## Anonymous function (lambda) with more than one argument.
print(multiply_lambda(3,6))

#DONE
 