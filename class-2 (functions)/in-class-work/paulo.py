### PLAYING WITH FUNCTIONS

## function with only no-named arguments.
def function_with_only_no_named_args(*args):
    print(args)
   #(try sending arguments i n diferent order when executing)
print('Ex #1')
function_with_only_no_named_args('one', 1, 'yes', 'whoo')
function_with_only_no_named_args('one', 'yes', 'whoo', 1)


## function with only named arguments.
def function_with_only_named_args(name, location, age=27):
   print(name, location, age)
   #(try sending arguments in diferent order when executing)
print('Ex #2')
function_with_only_named_args(name='Paulo', location='Chicago')

## function with both named and no-named arguments.
def function_with_both_named_no_named_args(arg, args, fixed_one='whoooo'):
   print(arg, args, fixed_one)
   #(named arguments must be on the right part of the argument list)
print('Ex #3')
function_with_both_named_no_named_args('1st arg', [2,3,4,5], fixed_one='yes')


## function using special *args and **kwargs arguments.
def function_using_special_args_kwargs(*args, **kwargs):
    print(args, kwargs)
print('Ex #4')
function_using_special_args_kwargs(1,2,3,4,5,6,7,8,9, paulo='paulo')
 
## function using some optional arguments.
def function_using_some_optional_args(*args1):
    print('this is args1', args1)
   #(try executing the funcion both sending and not sending the optional parameter)
print('Ex #5')
function_using_some_optional_args(1,2,3,4, ['a','b','c'])

## function using the "return" keywork. Assing the result of the function to a variable
def function_using_return(text):
    text_list = []
    if len(text)>1:
        for i in text.split():
            text_list.append(i)
    else:
        text_list.append(text)
    return text_list

print('Ex #6')
print(function_using_return('This is a test'))

## function that receives another function as argument and executes it.
def using_another_function(arg='a'):
    function_with_only_no_named_args(arg, 1, 2, 3)

print('Ex #6') 
using_another_function(2)
using_another_function()

## Assign an anonymous function (lambda) to a variable and execute it.
#my_sum = lambda x, y: x + y 

print('Ex #7')
weird_function = lambda x, y: x+y
print(weird_function('a','b'))


print('Ex #8')
## Anonymous function (lambda) with more than one argument.
weird_function_more_args = lambda x, *y: x+y
#print(weird_function_more_args('a','b','wh','o','o','o','o','o','o','o','o'))