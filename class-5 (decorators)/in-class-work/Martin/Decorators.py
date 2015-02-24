#1) implement a @small_arguments decorator for the "sum(a, b)" function, that raises ValueError if any of given arguments are greater than 10.

def small_arguments(s):
    def small_only(a, b):
        if a > 10 or b > 10:
            raise ValueError("arguments must be smaller than 10")
        return s(a, b)
    return small_only

#2) implement a @pretty_result decorator for the "sum(a, b)" function, that prints the result with this template: "The result was: XXX"

def pretty_result(r):
    def make_pretty(a,b):
        print("the result was: {}".format(r(a,b)))
    return make_pretty

#3) implement one of the previous decorator as a Class instead of function.

class make_me_pretty(object):
    def __init__(self, r):
        self.r = r
        
    def __call__(self, a, b):
        print("the result was: {}".format(self.r(a,b)))
        self.r(a,b)
        
    
#4) use both decorators together in the "sum(a, b)" function.        

#@pretty_result
@make_me_pretty
@small_arguments
def small_sum(a, b):
    return a+b
    
    
small_sum(2,6)