# New Line of Communication
When you were on the last level we discovered the aliens had been communicating with a human insider back on Earth, and by email of all things! Well, it seems that may have been a bit of a decoy as they're also exchanging secret encrypted messages from a server on one of the probe ships.

We need you to write a script which can connect over TCP to the following server ("localhost", 10000) and send 'GET' to retrieve the encrypted messages. You then need to decrypt them and send them back split by \n. We think you'll receive 3 sentences and they're encrypted with a caesar cipher that has a different random offset per sentence.

Finally, print the response after sending the decrypted messages to get the flag.

**Tip:** Remember, each encrypted message has a different random offset.

## Code
```python
import socket

wordList = ["SHE", "BEFORE", "HER", "YOU", "ARE", "VEIL", "HIS", "IT", "ME", "IN", "THE", "SO", "TO", "HE", "AT", "THEY"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 10000))
sock.send(b'GET')

data = sock.recv(1024).decode("utf-8")
sentences = data.split("\n")

answers = []
for index in range(1, 4):
    sentence = sentences[index]

    for index in range(1, 27):
        decrypted = ""

        for letter in sentence:
            shift = index

            if ord(letter) in range(65, 91):
                if ord(letter) + shift not in range(65, 91):
                    shift -= 26
                
                decrypted += chr(ord(letter) + shift)
            else:
                decrypted += letter
        
        for keyword in wordList:
            if keyword in decrypted:
                answers.append(decrypted)
                break

sock.send(bytes(answers[0] + "\n" + answers[1] + "\n" + answers[2], "utf-8"))
print(sock.recv(1024).decode())
```

![code output](/assets/screenshots/moon-08-NewLineofCommunication.png)