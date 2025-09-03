# Chilly Command
We know the hackers gained access to a particular Windows box, but we're not sure exactly what they did. See if you can use the registry file to figure out what the last command was that they ran.

**Tip:** Get the command to get the flag.

## Files
[HKEY_CURRENT_USER.reg.xml](/assets/files/HKEY_CURRENT_USER.reg.xml)

## Steps
1. Download and open the *.xml* file
1. Search for the word *RunMRU*
1. Decode the Base64-encoded command (*JwBUAGgAMwBfAEIAMwBzAFQAXwBGAGwANABnAHMAXwBSAF8ARgAwAHIAMwBuADUAMQBjACcA*)

![base64 decode](/assets/screenshots/fn-07-ChillyCommand.png)

4. Remove the � characters