i = open("input.txt", 'r')
o = open("output.txt", 'w')
oLine = i.readlines() 
i.close()
for line in oLine:
	if len(line) > 10:
		line = line[:-(len(line)-10)]+"\n"
	o.write(line)
o.close()