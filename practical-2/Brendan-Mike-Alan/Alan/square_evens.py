def square_of_evens(int_list):
	squared = map(lambda num: num**2, filter(lambda a: a % 2 == 0, int_list))
	return squared


## A little cleaner this time:

def square_evens(int_list):
	even = lambda a: a % 2 == 0
	squared = map(lambda num: num**2, filter(even, int_list))
	return squared




def test():
	assert square_of_evens([1,2,3,4,5,6,7,8,9,10]) == [4, 16, 36, 64, 100]
	assert square_evens([1,2,3,4,5,6,7,8,9,10]) == [4, 16, 36, 64, 100]

test()