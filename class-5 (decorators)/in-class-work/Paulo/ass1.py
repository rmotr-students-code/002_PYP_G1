#1) implement a @small_arguments decorator for the "sum(a, b)" function, 
#that raises ValueError if any of given arguments are greater than 10.


def small_arguments(f_sum):
    def only_small(a,b):
        if type(a) != int or type(b) != int:
            raise ValueError("Only int arguments!") # only ints
        if a > 10 or b > 10:
            raise ValueError("This is greater than 10 son")
        f_sum(a,b)
    return only_small


@small_arguments
def f_sum(a, b):
    print(a + b)    

#f_sum('hi', 'yo')
f_sum(6,6)
f_sum(11,11)