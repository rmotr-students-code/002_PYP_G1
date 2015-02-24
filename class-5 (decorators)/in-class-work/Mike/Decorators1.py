#1) implement a @small_arguments decorator for the "sum(a, b)" function, that raises ValueError if any of given arguments are greater than 10.

def small_arguments(f):
    def new_f(a, b):
        if a >10 or b > 10:
            raise ValueError("Arguments are greater than 10!")
        f(a, b)
    return new_f


@small_arguments
def sum(a, b):
    print (a + b) 
    

sum(12,1)


