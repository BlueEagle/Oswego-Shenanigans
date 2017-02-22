def toascii(text):
	table = []
	for x in text:
		table.append(ord(x))
	return table

def asciito(table):
	tempTable = []
	for x in table:
		tempTable.append(chr(int(x)))
	table = "".join(tempTable)
	del tempTable
	return table
	
def cls():
	import os
	os.system("cls")
	
def system(cmd):
	import os
	os.system(cmd)

def stringtoascii(string):
	string = string.replace("[","")
	string = string.replace("]","")
	string = string.replace(" ","")
	string = string.split(",")
	return string
	
	
cls()
end = 0
while not end == 1:
	answer = input("Choose one:\n1) Convert text to ascii.\n2) Convert ascii back to text.\n3) Convert an ascii table to text.\n\nAnswer: ")
	if answer == 1:
		cls()
		answer = raw_input("Enter your text here: ")
		cls()
		keytable = toascii(answer)
		print keytable
		system("pause")
		cls()
	if answer == 2:
		cls()
		text = asciito(keytable)
		print text
		system("pause")
		cls()
	if answer == 3:
		cls()
		answer = raw_input("Enter ascii table here: ")
		cls()
		text = asciito(stringtoascii(answer))
		print text
		system("pause")
		cls()