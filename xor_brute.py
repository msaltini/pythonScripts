import decode64

def xor_brute():
    x = input("Strinhg to crack")
    cipher = decode64.decode(x)
    plain = ""
    
    for i in range(0,256):
        for letter in cipher:
            plain += chr(ord(letter) ^ i)
        print(plain)
        plain =""

xor_brute()

