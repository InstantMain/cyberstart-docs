# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 16

PADDING = '{'

# Encrypted text to decrypt
encrypted = "uqX82PBZ8pi1fvt4GLHYgLs50ht8OQlrR1KHL2teppQ="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

secret = "password"

with open("words.txt", encoding="utf-8") as file:
    for secret in file:
        secret = secret[:-1]
        if len(secret.encode('utf-8')) >= 32:
            print("Error, string too long. Must be less than 32 bytes.")
        else:
            # create a cipher object using the secret
            key = (secret + (BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING).encode('utf-8')
            if len(key) != 16:
                continue

            cipher = AES.new(key, AES.MODE_ECB)

            # decode the encoded string
            decoded = decode_aes(cipher, encrypted)
            #print(decoded)

            if decoded.startswith('FLAG:'):
                print("\n")
                print("Success: "+secret+"\n")
                print(decoded+"\n")
                break
            else:
                print('Wrong password')
