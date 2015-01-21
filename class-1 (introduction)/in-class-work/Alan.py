"""
numList = [1,2,3,4]

numSet = set(numList)

numSet2 = {5,6,7,8}

print numSet
print "this is numSet before pop:" , numSet

print type(numSet)

pop_1 = numSet.pop()
pop_2 = numSet.pop()

print pop_1
print "This is {0}".format(pop_1)
print "this is pop 1: {0}, this is pop 2: {1}".format(pop_1, pop_2)

print "numSet after pop", numSet
"""

d = {
    'a': 1
}

for k in d:
    print(k)