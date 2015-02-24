def square_of_evens(nums):
    nums = filter(lambda x: x % 2 == 0, nums)
    return map(lambda x: x ** 2, nums)