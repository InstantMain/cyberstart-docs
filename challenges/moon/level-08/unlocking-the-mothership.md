# Unlocking the Mothership
Agent, it looks like the aliens' insider back on earth is someone with a good understanding of technology. The aliens have left him a very complicated backdoor into the ships control system, but we need your expertise to figure it out and break in. If we can do that we think we might be able to set the alien ship to self-destruct!

Write a script which connects to the server controlling the entry to the aliens' tech over TCP at localhost:10000 and send some random data. We've already tried it and it sends back a bunch of random word codes. There's also a file called backdoor.txt containing some random text. Use your script to encrypt a message using that text and the word codes. Each word is represented by: paragraph_number, line_number, word_number. We think sending the encrypted message back is what will unlock the server and give us access to the alien tech!

The server expects all the words in one transmission. The words should be stripped of punctuation and sent over separated by newline characters (\n). You'll need to look at the final server response to find the flag.

**Tip:** Send the encrypted message back to the server and look at the response to get the flag.

## Code
```python
import socket

backdoorFile = open("backdoor.txt", "r")
text = backdoorFile.read()
backdoorFile.close()

paragraphs = text.split("\n\n")
for index, paragraph in enumerate(paragraphs):
    paragraphs[index] = paragraph.split("\n")

    for j, line in enumerate(paragraphs[index]):
        paragraphs[index][j] = line.split(" ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 10000))
sock.send(b'some random data')

wordCodes = sock.recv(1024).decode().replace(",", "").split("\n")[0:6]
for index, wordCode in enumerate(wordCodes):
    wordCodes[index] = wordCode.split(" ")

message = ""
for wordCode in wordCodes:
    message += paragraphs[int(wordCode[0]) - 1][int(wordCode[1]) - 1][int(wordCode[2]) - 1].replace(".", "").replace("!", "").replace(",", "").replace("\"", "") + "\n"

sock.send(message.encode())
print(send.recv(1024).decode())
```

![code output](/assets/screenshots/moon-08-UnlockingtheMothership.png)