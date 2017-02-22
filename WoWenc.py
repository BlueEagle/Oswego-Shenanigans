def cls():
	import os
	os.system("cls")
def pause():
	import os
	os.system("pause")
def system(cmd):
	import os
	os.system(cmd)
def python():
	import os
	os.system("start python")
def asciito(table):
	tempTable = []
	for x in table:
		tempTable.append(chr(int(x)))
	table = "".join(tempTable)
	del tempTable
	return table
def backword(text):
	temp = []
	text = text.replace("", "BREAKSPACE_HOLDER")
	text = text.split("BREAKSPACE_HOLDER")
	ltext = len(text)
	for x in text:
		ltext = ltext - 1
		temp.append(text[ltext])
	text = "".join(temp)
	del temp
	return text
	del text

password = [535268503, 360486951, 360486951, 360486951, 1179775476, 1212547017, 1212547017, 1136080088, 1081460853, 906679301, 1245318558, 1103308547, 1190699323, 1190699323, 1278090099, 906679301]
# This has long since changed by the way. ^^^

cls()
print "_________________________"
print " Hello and welcome back! "
print "=========================\n\n"
key = input("Key: ")
for x in range(0,len(password)):
    password[x] = password[x]/key
password = asciito(password)
password = backword(password)
cls()
print "Results:\n\n", password,"\n\n\n\n"
pause()
