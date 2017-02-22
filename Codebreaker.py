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
    del table
def collect(text):
    text = raw_input(text)
    text = text.replace(" ","")
    text = text.split(",")
    return text
    del text
end = 0
while end == 0:
    cls()
	print ""