# Nightclub Rendezvous
Agent 707, this one is urgent. Our team have just intercepted some chatter between two gang members and it's confirmed they are holding a meeting tonight at a nightclub somewhere in London. Unfortunately there are a lot of nightclubs in London and they didn't mention which one. Then, 10 minutes after the conversation ended, one of them posted up a cryptic piece of text on his social media account. We think it contains the time and exact location of the meeting. We have every agent on the ninth floor working to decode the text, can you get there first?

Here's what we know about it so far: each character in the text was converted into a decimal number (according to the ASCII chart), then each number had the same number subtracted from it (a number between 1 and 10). Then each number was written to a new line of the text.

**Tip:** The flag is the name of the nightclub.

## Steps
1. Write python code
    - Copy the numbers listed on the page and format them into an array

```python
decimals = [
    81,
    95,
    33,
    108,
    95,
    26,
    103,
    95,
    95,
    110,
    99,
    104,
    97,
    26,
    91,
    110,
    26,
    110,
    98,
    95,
    26,
    60,
    91,
    92,
    91,
    108,
    111,
    109,
    101,
    99,
    26,
    104,
    99,
    97,
    98,
    110,
    93,
    102,
    111,
    92,
    26,
    99,
    104,
    26,
    70,
    105,
    104,
    94,
    105,
    104,
    26,
    91,
    110,
    26,
    43,
    43,
    106,
    103,
    26,
    110,
    98,
    99,
    109,
    26,
    95,
    112,
    95,
    104,
    99,
    104,
    97,
    40
]

for number in range(1, 11):
    result = ""
    for decimal in decimals:
        result += chr(decimal + number)
    print(result + "\n")
```
 
2. Run the python code
    - The flag is the name of the nightclub

![decoded ASCII](/assets/screenshots/hq-11-NightclubRendezvous.png)