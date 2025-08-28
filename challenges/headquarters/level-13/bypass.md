# Bypass
Agent 707, we've found a TCP service the gang are using, but we can't seem to get access. It's services.cyberprotection.agency on port 13880 See if you can bypass the login screen and begin exploring.

## Steps
1. Netcat the server
    - Use *nc* command on *services.cyberprotection.agency* with port *13880*

![source code](/assets/screenshots/hq-13-Bypass/step-1.png)

2. Hold the *Enter* key on your keyboard until it says *Welcome \<uninitialized>.*

![source code](/assets/screenshots/hq-13-Bypass/step-2.png)

3. List the available commands with the *?* command

![source code](/assets/screenshots/hq-13-Bypass/step-3.png)

4. Use the flag command

![source code](/assets/screenshots/hq-13-Bypass/step-4.png)