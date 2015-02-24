"""### Min max
Given a list of integers return the largest and the smallest values.
"""

def max_min(input1, max_min):
    if max_min == "Max" or max_min == "MAX" or max_min == "max":
        return max(input1)
    elif max_min == "Min" or max_min == "MIN" or max_min == "min":
        return min(input1)

print max_min([1,2,13,413,3,413,1,-123], "Max")