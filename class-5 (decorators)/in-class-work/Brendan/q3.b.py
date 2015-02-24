class make_pretty(object):
    def __init__(self, sum_):
        self.sum_ = sum_
    
    def __call__(self, a, b):
        print 'The result was: {}'.format(self.sum_(a, b))

@make_pretty
def sum(a, b):
    return a + b
    
sum(2, 4)