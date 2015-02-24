#3) implement one of the previous decorator as a Class instead of function.

class small_arguments(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, a, b):
        if a > 10 or b > 10:
            raise ValueError("Arguments greater than!")
        self.f(a, b)


@small_arguments
def sum(a, b):
    print (a + b) 
    

sum(9,1)