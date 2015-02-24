def countName(filename):
	namedict = {}
	with open('{}'.format(filename)) as f:
		for line in f:
			name, num1, num2, idnum = [item for item in line.split()]
			if name[0] not in namedict:
				namedict[name[0]] = 1
			else:
				namedict[name[0]] += 1
	return namedict

print countName('names.txt')