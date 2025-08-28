# Port of Call
Quick job for you Agent 707. We think the gang have a port running between 14000 and 15000 that might expose some interesting information about them, we've temporarily pointed our domain services.cyberprotection.agency to their server. Use that address to find the service and connect to it.

**Tip:** Connect to the port to get the flag.

## Steps
1. Use *nmap* to scan for open ports from port *14000* to port *15000* on *services.cyberprotection.agency*

![nmap scan](/assets/screenshots/hq-11-PortofCall/step-1.png)

2. Use *nc* to connect to the port

![man page descrption](/assets/screenshots/hq-11-PortofCall/step-2.png)