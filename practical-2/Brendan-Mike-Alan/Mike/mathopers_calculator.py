def sum_(nums):
    return reduce(lambda a,b: a + b, nums)
    
def subtract_(nums):
    return reduce(lambda a,b: a - b, nums)
    
def calculator(op,*args):
    return op(args)