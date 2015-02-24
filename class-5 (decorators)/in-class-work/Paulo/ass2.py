#2) implement a @pretty_result decorator for the "sum(a, b)" function, 
# that prints the result with this template: "The result was: XXX"


def pretty_result(f_sum):
    def prints_pretty(a,b):
        if type(a) != int or type(b) != int:
            raise ValueError("Only int arguments!") # only ints
        if a > 10 or b > 10:
            raise ValueError("This is greater than 10 son")
        
        print("The result is {}".format(f_sum(a,b))
    
        return prints_pretty
    # return print("The result is {}".format(f_sum(a,b))


@pretty_result
def f_sum(a, b):
    return (a + b)    

#f_sum('hi', 'yo') - ok
f_sum(6,6) - ok
#f_sum(11,11) - ok



