def minmax(nums):
    min_ = lambda a,b: a if (a > b) else b
    min1_ = reduce(min_,nums)
    max_ = lambda a,b: a if (a < b) else b
    max1_ = reduce(max_,nums)
    return min1_, max1_
    
    
    
def minmax1(nums):
    min_ = reduce(lambda a,b: a if (a > b) else b, nums)
    max_ = reduce(lambda a,b: a if (a < b) else b, nums)
    return min_, max_