def line_num(name):
	number = 0
	location = []
	formatted = name.lower()
	with open('names.txt', 'r') as f:
		for line in f:
			if line.split()[0].lower() == formatted:
				location.append(number)
			number += 1
	return location