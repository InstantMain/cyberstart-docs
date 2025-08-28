# Fork in the Road
Agent 707, it's time we went on the offensive! We know the Bulldogs are putting their trojan horse robot plan into action, and whilst we're continuing to work specifically on stopping that we also want to disrupt as many of the Bulldogs operations as possible, to keep them distracted and slow them down.

Here's one example we want your help with specifically. Remember the encryption tool Cryptonite that one of the Bulldogs created from the previous level? It uses server side commands to handle the encryption and we want you to use some kind of command injection to send the command for a fork bomb to DoS the website and take down the tool.

## Steps
1. Enter in *;cryptonite -h* and click *Enter* to show its arguments
    - *;cryptonite -n* can be used to ignore the command and for command injection

![show arguments](/assets/screenshots/hq-12-ForkintheRoad/step-1.png)

2. Enter in *;cryptonite -n; :(){ :|:& };:* and click *Enter*
    - *:(){ :|:& };:* is a bash function used for denial-of-service attacks (called the *fork bomb*)

![DoS input](/assets/screenshots/hq-12-ForkintheRoad/step-2.png)