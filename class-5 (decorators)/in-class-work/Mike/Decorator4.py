#4) use both decorators together in the "sum(a, b)" function.

def small_arguments(f):
    def new_f(a, b):
        if a >10 or b > 10:
            raise ValueError("Arguments are greater than 10!")
        f(a, b)
    return new_f

def pretty_result(f):
    def new_f(a, b):
        f(a, b)
    return "The result was: {}.".format(new_f)


@small_arguments
@pretty_result
def sum(a, b):
    print (a + b) 
    

sum(12,1)