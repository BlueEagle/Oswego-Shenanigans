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