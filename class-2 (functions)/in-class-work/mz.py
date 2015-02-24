# THIS IS:


# named arguments
def sum(a, b):
    return a + b
    
sum(a=1, b=2)  # 3
sum(1, 2)  # 3



# DIFFERENT TO:


# default arguments
def sum(a=1, b=2):
    return a + b
    
sum()  # 3
sum(a=10)  # 12
sum(a=10, b=20)  # 30