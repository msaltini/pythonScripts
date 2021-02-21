import xor_brute

file = open("C:\\Users\\Matteo\\Downloads\\5_10ab6c2a0ce05c7c7bdfcf9e5b229adf.05.txt", 'r')
for x in file:
    data = file.readline().replace('\n', '')
    xor_brute.xor_brute(data)

file.close()