import base64

def encode(x):
    base64_bytes = x.encode('ascii')
    base64_encode = base64.b64encode(base64_bytes)
    encoded_message = base64_encode.decode('ascii')
    print(encoded_message)

x = input('String to encode:')
encode(x)