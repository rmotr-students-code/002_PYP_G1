

def average(*args):
	""" Takes the average of the arguments passed, whether those arguments
		are lists, ints or a mix of both. """
	num_items = 0.0
	added = 0.0
	for item in args:
		if isinstance(item, list):
			added = sum(item)
			num_items += len(item)
		else:
			added += item
			num_items += 1
	return added / num_items


def test():
	assert average(1,5,3,2) == 2.75
	assert average([1,5,3,2]) == 2.75
	assert average([1,5,3],2) == 2.75

test()

