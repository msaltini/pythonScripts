import base64

def decode():
    x = input('String to decode:')
    base64_bytes = x.encode('ascii')
    base64_message = base64.b64decode(base64_bytes)
    message = base64_message.decode('ascii')
    print(message)

decode()
