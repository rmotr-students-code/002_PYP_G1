'''### Average

Write a function that can either receive a list or different integer arguemnts and computes the Average:

Example:

    average(1, 5, 3, 2)  # 2.75
    average([1, 5, 3, 2]) # 2.75
'''

def average(*args):
    sum_ = 0
    count = 0
    if isinstance(args[0], list):
        for x in args[0]:
            sum_ += x
        length = len(args[0])
    else:
        for x in args:
            sum_ += x
            count += 1
        length = count
    return float(sum_) / length

print average(1,5,3,2)
            
    