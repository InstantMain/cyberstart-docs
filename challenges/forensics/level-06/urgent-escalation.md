# Urgent Escalation
Ok, urgent work for you, Agent 707 - this case just got escalated up through the ranks. As you've been looking into it again I decided to get a couple of other agents to take a look as well and they've noticed something of serious concern - we believe one of the servers in our Brazilian office which we were using to conduct the initial investigation has been compromised by exploiting a potential vulnerability. Can you identify it from the log files?

**Tip:** Find the vulnerability to get the flag.

## Files
[access.log](/assets/files/access.log)

## Steps
1. Download and open the log file
1. Find the suspicious log result 
    - *192.168.29.136 - - [17/Sep/2018:03:17:36 -0700] "GET /usr/lib/cgi-bin/basic.sh HTTP/1.1" 404 461 "-" "() { :;};echo -e \"\\r\\nU2gzbGxfU2gwY2tlZF9ieV9TMW1wbDFjMXR5IQo=$(/tmp/dJWhq)U2gzbGxfU2gwY2tlZF9ieV9TMW1wbDFjMXR5IQo=\""*
1. Extract *U2gzbGxfU2gwY2tlZF9ieV9TMW1wbDFjMXR5IQo=* from the result and *Base64* decode it

![base64 decode](/assets/screenshots/fn-06-UrgentEscalation.png)