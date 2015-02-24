# 2) implement a @pretty_result decorator for the "sum(a, b)" function, that prints the result with this template: "The result was: XXX"

def pretty_result(f):
    def make_pretty(a, b):
        print 'The result was: {}'.format(f(a, b))
    return make_pretty

@pretty_result
def sum_(a,b):
    return (a + b)
    
sum_(11,3)