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
def toascii(text):
	table = []
	for x in text:
		table.append(ord(x))
	return table
cls()
message = raw_input("Type the message to encrypt: ")
cls()
key = input("Now type the key to decrypt your message: ")
message = backword(message)
message = toascii(message)
for x in range(0,len(message)):
    message[x] = message[x]*key
cls()
print "Your encrypted message is:\n\n", message, "\n\n\n\n"
pause()