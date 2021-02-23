import binascii

def xor_brute(x):
    xToHex = binascii.unhexlify(x)
    plain = []
    string = []
    ar = "C"
    for key in ar:
        for num in xToHex:
            plain.append(chr(num ^ ord(key)))
        plainText = ''.join(plain)
        string.append(plainText)
        plain = []
    return string

#cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
#xor_brute(cipher)

