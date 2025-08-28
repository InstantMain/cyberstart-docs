# Stop and Search
Agent 707, with all of the knowledge we have gathered about the trojan robot and the gang's plans for it we have been working with the bank to improve their security. We're currently doing penetration tests on all their internal systems and we've identified a possible XSS flaw in their contact management system, in the contact search field to be specific.

Here's a javascript payload, see if you can get it to work in the search field.

`<script>alert('Search this!!!')</script>`

Once this flaw has been fixed we are confident that the trojan robot the gang have been planning to send will have no effect on the banks system therefor rendering it useless! Good luck!

## Steps
1. Encode *\<script>alert('Search this!!!')</script>* to hexadecimal

![hexadecimal encoding](/assets/screenshots/hq-12-StopandSearch/step-1.png)

2. Copy and paste the encoded script in the *Name or email* text box

![script input](/assets/screenshots/hq-12-StopandSearch/step-2.png)

3. Click *Search*
1. The alert pops up, click the *OK* button

![alert popup](/assets/screenshots/hq-12-StopandSearch/step-3.png)