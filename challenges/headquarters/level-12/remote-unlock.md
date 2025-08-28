# Remote Unlock
Agent 707, it seems the robot the gang want to send to the bank will first need to undergo a series of tests which we are hoping will reveal more information about how they will activate the robot once it arrives at the bank.

They seem to be testing it with a server (which we've pointed services.cyberprotection.agency at, port 9999), which has a service running on it. When you connect it starts a timer and gives you three numbers. We think to unlock it you need to multiply the first two numbers together and then divide the result by the third number. But the integer result has to be sent to the server in under 1 second to gain access to the remote package. We haven't been able to find a way to do it. Can you?

## Steps
1. Write Python code

```python
import socket

SERVER = "services.cyberprotection.agency"
PORT = 9999
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER, PORT))

    numbers = sock.recv(1024).decode()
    numbersSplit = numbers.split("\n")

    firstNum, secondNum, thirdNum = int(numbersSplit[0]), int(numbersSplit[1]), int(numbersSplit[2])
    result = int((firstNum * secondNum)/thirdNum)

    sock.send(str(result).encode())
    print(sock.recv(1024))
```

![python for service connection](/assets/screenshots/hq-12-RemoteUnlock.png)