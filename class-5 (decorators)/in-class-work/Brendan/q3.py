# 3) implement one of the previous decorator as a Class instead of function.

class small_arguments(object):
    def __init__(self, small_sum):
        self.small_sum = small_sum
        self.arg1
    
    def __call__(self, a, b):
        if a > 10 or b > 10:
            raise ValueError('Arguments must be smaller than 10!')
        self.small_sum(a, b)
        
        
@small_arguments
def sum(a, b):
    print a + b
    
sum(299, 5)