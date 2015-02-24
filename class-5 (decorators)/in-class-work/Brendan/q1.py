# 1) implement a @small_arguments decorator for the "sum(a, b)" function, that raises ValueError if any of given arguments are greater than 10.

def small_arguments(f):
    def check_args(a, b):
        if a > 10 or b > 10:
            raise ValueError('Arguments must be less than 10!')
        f(a, b)
    return check_args

@small_arguments
def sum(a, b):
    print (a + b)



sum(1, -12)