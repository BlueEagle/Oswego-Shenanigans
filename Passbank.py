# Global vars:
entropy = 25 # The entropy is the encryption complexity, try to keep this a two digit number. Higher entropy is higher security, but takes more power to process.
# *** NEVER SET ENTROPY TO: 0 ***
# Block #10
def toascii(text):
    table = []
    for x in text:
        table.append(ord(x))
    return table
# Block #11
def stringtolist(string):
    list = string
    list = list.replace("[","")
    list = list.replace("]","")
    list = list.replace(" ","")
    list = list.split(",")
    return list
    del string
    del list
# Block #20
def asciito(table):
    tempTable = []
    for x in table:
        tempTable.append(chr(int(x)))
    table = "".join(tempTable)
    del tempTable
    return table
    del table
# Block #21
def listtostring(list):
    string = ""
    for x in range(0,len(list)):
        string = string + list[x]
    return string
    del list
    del string
# Block #30
def backword(text):
    counter = len(text) - 1
    txet = ""
    for x in range(0,len(text)):
        txet = txet + text[counter]
        counter = counter - 1
    return txet
    del text
    del txet
# Block #31
def intliststrlist(list):
    for x in range(0,len(list)):
        list[x] = str(list[x])
    return list
# Block #40
def rawvalue(text):
    text = toascii(backword(text))
    return text
# Block # 50 
def pullkey(text):
    text = rawvalue(text)
    text = int(text)/100000
    return int(text)
# Block # 60
def encrypt(key,text):
    key = pullkey(key)
    text = toascii(backword(text))
    for x in range(0,len(text)):
        text[x] = text[x]*key/2
    del key
    return text