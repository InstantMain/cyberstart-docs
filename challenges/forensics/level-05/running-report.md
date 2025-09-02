# Running Report
Ok agent, it's time to start putting together a draft of the report we'll send on to the client and there's some specific information we need that you can help with. We have found the first time and date the hacker attempted to connect to our client's networks, but we cannot determine what their first actions were. Take a look at the network traffic and then see if you can use it to fill out the forensics report form.

**Tip:** Answer the questions to get the flag.

## Files
[port scan.pcapng](</assets/files/port scan.pcapng>)

## Steps
1. Download and open the *.pcapng* file in Wireshark
1. Notice that the port scan looks at a single IP address
    - Reconnaissance scan is *Vertical*

![IP addresses](/assets/screenshots/fn-05-RunningReport/step-1.png)

3. Filter for *tcp.flags == 0x010*
    - This filters for all TCP packets with only the *ACK* flag

![filtered packets](/assets/screenshots/fn-05-RunningReport/step-2.png)
 
4. The six open ports are the destination ports of the six packets filtered for (*135, 139, 445, 5357, 6666, 7443*)
1. Notice that some of the open ports are designed for Windows
    - Operating system installed is *Windows*

![answers to questions](/assets/screenshots/fn-05-RunningReport/step-3.png)