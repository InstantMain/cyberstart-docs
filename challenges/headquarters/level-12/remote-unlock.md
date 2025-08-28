# Remote Unlock
Agent 707, it seems the robot the gang want to send to the bank will first need to undergo a series of tests which we are hoping will reveal more information about how they will activate the robot once it arrives at the bank.

They seem to be testing it with a server (which we've pointed services.cyberprotection.agency at, port 9999), which has a service running on it. When you connect it starts a timer and gives you three numbers. We think to unlock it you need to multiply the first two numbers together and then divide the result by the third number. But the integer result has to be sent to the server in under 1 second to gain access to the remote package. We haven't been able to find a way to do it. Can you?

## Steps
1. Write Python code

![python for service connection](/assets/screenshots/hq-12-RemoteUnlock.png)