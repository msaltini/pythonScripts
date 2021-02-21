import binascii

def xor_brute(x):
    xToHex = binascii.unhexlify(x)
    plain = []
    
    for key in range(256):
        for num in xToHex:
            plain.append(chr(num ^ key))
        print(''.join(plain))
        plain = []

cipher = input("String to crack:")
xor_brute(cipher)

