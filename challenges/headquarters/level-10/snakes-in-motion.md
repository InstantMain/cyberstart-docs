# Snakes in Motion
Agents have intercepted some vital information we'd like you to look at. We've sent you an email with some encrypted text, a dictionary file and a Python script to help you extract what we believe might be the password to a cloud storage solution the Spetzners use to store their criminal documents. One problem, unfortunately, the Python script is incomplete.

Can you finish it off so that it runs each line in the dictionary against the encrypted text to decrypt it? Hurry agent, the Spetzners might know we are on to them and could transfer their documents elsewhere!

## Files
[dict.py](/assets/files/dict.py)    
[words.txt](/assets/files/words.txt)

## Steps
1. Fixed python code

```python
# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "uqX82PBZ8pi1fvt4GLHYgLs50ht8OQlrR1KHL2teppQ="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

with open("words.txt", "r", encoding="utf-8") as file:
    for secret in file:
        secret = secret.strip()
        if secret[-1:] == "\n":
            print("Error, new line character at the end of the string. This will not match!")
        elif len(secret.encode("utf-8")) >= 32:
            print("Error, string too long. Must be less than 32 bytes.")
        else:
            # create a cipher object using the secret
            key = (secret + (BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING).encode('utf-8')

            cipher = AES.new(key, AES.MODE_ECB)

            # decode the encoded string
            decoded = decode_aes(cipher, encrypted)

            if decoded.startswith('FLAG:'):
                print("\n")
                print("Success: "+secret+"\n")
                print(decoded+"\n")
                break
            else:
                print('Wrong password')
```

2. Run the python code

![run python code](/assets/screenshots/hq-10-SnakesinMotion/step-1.png)

![decrypted password](/assets/screenshots/hq-10-SnakesinMotion/step-1.1.png)