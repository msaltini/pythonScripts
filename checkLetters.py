import string

def getLine(file):
    for number, line in enumerate(file):
        for c in line:
            if c not in string.printable:
                break
            return number

file = open("result.txt", "r", encoding="utf-8")
print(getLine(file))
file.close()
