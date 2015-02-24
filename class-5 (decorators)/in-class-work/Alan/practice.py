#1) implement a @small_arguments decorator for the "sum(a, b)" 
#   function, that raises ValueError if any of given arguments are greater than 10.
#2) implement a @pretty_result decorator for the "sum(a, b)" function, 
 #   that prints the result with this template: "The result was: XXX"
#3) implement one of the previous decorator as a Class instead of function.
#4) use both decorators together in the "sum(a, b)" function. 



def small_arguments(function):
    def test(a, b):
        if a > 10 or b > 10:
            raise ValueError("These arguments must be less than 10!")
        return function(a, b)
    return test
    
def pretty_result(function):
    def prettify(a, b):
        print "The result was: {}".format(function(a,b))
    return prettify

class Small_ArgumentsV2(object):

    def __init__(self, function):
        self.function = function
    
    def __call__(self, a, b):
        if a > 10 or b > 10:
            raise ValueError("Nope")
        return self.function(a, b)
    
 
@pretty_result
@Small_ArgumentsV2
def sum(a, b):
    return a + b
    
print sum(1, 2)

    
    #the result was: None