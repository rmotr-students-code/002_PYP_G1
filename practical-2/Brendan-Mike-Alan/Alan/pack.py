def build_list(*args):
	listy = []
	for item in args:
		listy.append(item)
	return listy

## test

print build_list(1,2,3,'pop','stop')
