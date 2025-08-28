# Bogdan's Data
Agent 707, a possible breakthrough that we need your help with. We've found a server run by the gang, it's at services.cyberprotection.agency:3166 and it seems to be protecting some data. The gang member who we think administers it, Bogdan, is one of the key members behind the plans to steal the EMP. We think it might have even been his suggestion in the first place. In short, we need access to the data on that server.

Fortunately we've been able to recover some source code for it. Take a look at the source code and see if you can get access to the server.

## Files
[evalserver_fragment.py](/assets/files/evalserver_fragment.py)

## Steps
1. Open the given python file
    - From the python code, it is deduced that the server will ask the client for the first number (can be any number), it will ask for the second number, and the modified first number and the given second number need to be equivalent to get the flag
    - The *eval* function parses the string passed to this into valid python code and runs it within the program in the current scope

```python
clientsock.send("Welcome to Maths_Server 1.0\n")

try:
    clientsock.send("Enter the first number, so I can EVALuate it:\n")
    firstNum = eval(clientsock.recv(1024))
    firstNum = firstNum + firstNum + ord(flag[4]) + ord(flag[8]) + ord(flag[5])
    clientsock.send("Enter the second number, so I can EVALuate it:\n")
    secondNum = eval(clientsock.recv(1024))
    if secondNum == firstNum:
        clientsock.send("The flag is: " + flag + "\n")
        firstNum = 0
        secondNum = 0
except:
    pass

clientsock.close()
```

2. Launch the virtual box and open terminal
1. Netcat server
    - Use *nc* command on *services.cyberprotection.agency* with port *3166*
1. Type in any number for the first number *(firstNum)*
1. Type in *firstNum* for the second number *(secondNum)*

![listen to server](/assets/screenshots/hq-09-Bogdan'sData.png)