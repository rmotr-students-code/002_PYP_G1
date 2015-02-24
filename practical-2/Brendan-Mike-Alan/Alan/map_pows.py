

def powers(items, power=2):
	""" Returns list of items raised to specified power
		which is passed as the 2nd argument. default is
		power of 2."""
	squared = map(lambda a: a**power, items)
	return squared



def test():
	assert powers([1,2,3]) == [1,4,9]
	assert powers([1,2,3],3) == [1,8,27]
	assert powers([1,2,3],power=3)==[1,8,27]

test()
