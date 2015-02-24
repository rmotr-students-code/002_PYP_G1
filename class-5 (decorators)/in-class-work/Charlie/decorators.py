# 1) implement a @small_arguments decorator for the "sum(a, b)" function, that raises ValueError if any of given arguments are greater than 10.
# 2) implement a @pretty_result decorator for the "sum(a, b)" function, that prints the result with this template: "The result was: XXX"
# 3) implement one of the previous decorator as a Class instead of function.
# 4) use both decorators together in the "sum(a, b)" function.

def small_arguments(f):
    
    def small_check(a, b):
        if int(a) > 10 or int(b) > 10:
            raise ValueError("Arguments can't be larger than 10.")
        else:
            return f(a, b)
    return small_check
    
    
class PrettyResult(object):
    
    def __init__(self, f):
        self.f = f
        
    def __call__(self, a, b):
        total = self.f(a, b)
        return "The result is: {}".format(total)



@PrettyResult
@small_arguments
def sum(a,b):
    return a + b
    
print(sum(1,12))