#!/usr/bin/env python3.9
import sys
import pyautogui
from Crypto.Cipher import AES
from base64 import b64decode
from hashlib import md5
from pyzbar.pyzbar import decode
from PIL import Image
from pwn import args
 
if args.SCREENSHOT:
	screen = pyautogui.screenshot()
	screen.save("./code.png")

data = decode(Image.open("./code.png"))	
decoded_qr = data[0].data.decode()
print(decoded_qr)

encoded_keys = decoded_qr.split("\n")
key = b""
ciphertext = b""

for count, string in enumerate(encoded_keys):
	if string != "":
		if count == 0:
			ciphertext += string[7:].encode("utf-8")	
			key += string[7:].encode("utf-8")
			continue
		ciphertext += b64decode(string[7:])


iv = b"\xb5\xcdt\xe0\x91\xdb8V\x10\xbf\xab;'\xd8\xe9\x8a" 
cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = cipher.decrypt(ciphertext)
print(plaintext.decode("ISO-8859-1"))
