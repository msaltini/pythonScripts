import xor_brute

file = open("C:\\Users\\Matteo\\Downloads\\5_10ab6c2a0ce05c7c7bdfcf9e5b229adf.05(1).txt", 'r')
file1 = open("result.txt", "x", encoding="utf-8")
for x in file:
    data = file.readline().replace('\n', '')
    strings = xor_brute.xor_brute(data)
    for string in strings:
        file1.write(string)
        file1.write("\n")
        #print(string)    
    file1.write("\n")

file.close()