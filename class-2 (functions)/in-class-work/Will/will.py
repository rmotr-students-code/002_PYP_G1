
   

   




 
# ## function using some optional arguments.
#    (try executing the funcion both sending and not sending the optional parameter)



# ## function using the "return" keywork. Assing the result of the function to a variable

def add(a, b):
   return a + b

result = add(5, 10)
print(result)
 
# ## function that receives another function as argument and executes it.
def name(name):
   return name

def say(name('will')):
   print('my name is: ' + name)
 
# ## Assign an anonymous function (lambda) to a variable and execute it.
 
# ## Anonymous function (lambda) with more than one argument.
 