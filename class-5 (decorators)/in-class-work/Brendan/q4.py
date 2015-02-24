def big_args(sum_):
    def check_args(a, b):
        if a > 10 or b > 10:
            raise ValueError('Arguments must be less than 10!')
        print 'The result was: {}'.format(sum_(a, b))
        sum_(a, b)
    return check_args
    
@big_args
def sum(a, b):
    return a + b

sum(1,21)