# numbers in a file, find which add two 2020 and then multiply them to find answer

inpFile = open('numbers.txt', 'r')
lines = inpFile.readlines()
lines = sorted(lines)
found = False
for i in lines:
	i = int(i)
	for j in lines:
		j = int(j)
		for aids in lines:
			aids = int(aids)
			if i + j + aids == 2020:
				print(i * j * aids)
				found = True
				break
		if found:
			break
	if found:
		break
