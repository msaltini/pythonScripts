#!/usr/bin/env python3
from Crypto.Cipher import AES 
from base64 import b64decode

key = b"What is the key?"
iv = b"\xd3\x8f\xcd\xa2\xe8\xb6*\x939\x18\x81\xb2P\xe1\xdaN"
ciphertext = (b'What is the key?'
	        + b64decode("t8DnV+HDpVm9EyOY2nUfxA==") 
            + b64decode("kmrMSsSaaSvbbVz3yW0zaw=="))

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
print(f"Plaintext is: \n{plaintext.decode('ISO-8859-1')}")
