# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

# Decodes the AES encryption text
def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e))#.decode('latin-1').rstrip(PADDING)

# Open the file with the words
with open("words.txt", encoding="utf-8") as file:
    for secret in file: # Go through each word
        secret = secret.strip() # Remove whitespaces
        if secret[-1:] == "\n":
            print("Error, new line character at the end of the string. This will not match!")
        elif len(secret.encode("utf-8")) >= 32:
            print("Error, string too long. Must be less than 32 bytes.")
        else:
            # Create a cipher object using secret
            cipher = AES.new(secret.encode("utf-8") + ((BLOCK_SIZE - len(secret.encode("utf-8")) % BLOCK_SIZE) * PADDING).encode("utf-8"), AES.MODE_ECB)

            # Decode the encrypted string using the cipher
            decoded = decode_aes(cipher, encrypted)

            try: # Attempt to decode the string
                decoded.decode()
            except: # If decoding errors, go to the next word
                continue
            else: # If no errors occur, print the decrypted flag and break the loop
                print(decoded.decode().rstrip(PADDING))
                break