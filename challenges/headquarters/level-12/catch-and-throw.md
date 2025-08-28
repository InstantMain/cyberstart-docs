# Catch and Throw
Agent 707, we've just stumbled on something we think could be very important. We know the gang have been working on getting their trojan horse robot into the bank, and we also know they're trying to communicate with it and use it to get access to the banks servers from the inside. But until now we didn't know if they had the codes they'd need once they'd made the connection. Well, it seems they might.

We've received an anonymous tip from one disgruntled gang member about two web pages, the second of which he claims, has a list of access codes the gang would need to get in. If we could see those codes we'd know whether the risk was real, but here's the thing - on the first web page there's just a number which keeps changing. On the second page, nothing, except for an error message. We think to open up access to the second page you need to pass the value from the first page to the cookie on the second page. Give it a try.

## Steps
1. Write Python code
    - The flag is the code at the bottom of the codelist

```python
import requests, re

SPINNER_URL = "https://bulldoghax.com/secret/spinner"
CODES_URL = "https://bulldoghax.com/secret/codes"

html = requests.get(SPINNER_URL).text
spinner_number = re.search("(\d+)", html).group()
codes_html = requests.get(CODES_URL, cookies = {"timelock": spinner_number}).text
print(codes_html)
```

![python to get most recent code](/assets/screenshots/hq-12-CatchandThrow.png)