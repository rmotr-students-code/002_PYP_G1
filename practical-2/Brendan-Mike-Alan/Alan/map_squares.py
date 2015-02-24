def squares(items):
	squared = map(lambda a: a**2, items)
	return squared


def test():
	assert squares([1,2,3]) == [1,4,9]

test()