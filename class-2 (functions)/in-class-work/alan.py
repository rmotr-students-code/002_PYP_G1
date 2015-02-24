### PLAYING WITH FUNCTIONS

## function with only no-named arguments.
def no_name(*args):
    for arg in args:
        print arg
        
no_name('hi','os','run')
#(try sending arguments i n diferent order when executing)

## function with only named arguments.
# (try sending arguments in diferent order when executing)
def only_names(name1, name2):
    return name1 + name2

print only_names(name1='nam1', name2='nam2')
print only_names(name2 = 'nam2', name1 = 'nam1')
#
## function with both named and no-named arguments.
#  (named arguments must be on the right part of the argument list)
def hetero_args(name, *args):
    return name, args
 
print hetero_args('Alan', 1, 2, 3)
#('Alan', (1,2,3))

## function using special *args and **kwargs arguments.
def person_list(*args, **kwargs):
    persons = kwargs
    return persons, args

print person_list(2, person1='Alan', person2='Dan')
#({'person2': 'Dan', 'person1': 'Alan'}, (2,))
 
## function using some optional arguments.

def options(string, num = 3):
    return string * num
    
print options('Hello', 5)

print options('hello')
 #  (try executing the funcion both sending and not sending the optional parameter)

## function using the "return" keywork. Assing the result of the function to a variable
def returny(string, number):
    return string * number

two_alans = returny('Alan', 2)

## function that receives another function as argument and executes it.
def runsFunc(func):
    return func()

def add():
	return 2 + 2

print runsFunc(add)
# 4
 
## Assign an anonymous function (lambda) to a variable and execute it.
lamdbastyle = lambda a: a + 2

lambdastyle(5)

lamdbaArgs = lambda *args: sum(args)

lambdaArgs(1,2,3,4,5)


 
 
## Anonymous function (lambda) with more than one argument.