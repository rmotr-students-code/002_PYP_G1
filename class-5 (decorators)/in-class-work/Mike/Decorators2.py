#2) implement a @pretty_result decorator for the "sum(a, b)" function, that prints the result with this template: "The result was: XXX"

def pretty_result(f):
    def new_f(a, b):
        print "The result was: {}".format(f(a,b))
    return new_f

@pretty_result
def sum(a, b):
    return (a + b) 
    

sum(8,1)
