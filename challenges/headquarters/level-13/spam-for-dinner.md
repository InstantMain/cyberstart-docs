# Spam For Dinner
Agent 707, we're trying to distract the gang whilst we try and gain access to their primary server and we think we've found a target for you.

We want to spam the booking form for their restaurants, the problem is the form is protected by a Captcha. You may be able to bypass the Captcha by tricking the form into using a different Captcha value; and if you can do so at least 5 times, that'll prove a successful bypass for the bot we'll create!

## Steps
1. View the page’s source code
    - It shows that the value for *seedID* determines the captcha

![source code](/assets/screenshots/hq-13-SpamForDinner/step-1.png)

2. Set the second query string value for *seedID* by appending *&seedID=* followed by 4 random numbers separated by colons in the URL after *venue=shanghai*
    - e.g. *&seedID=1:1:1:1*

![query string appended](/assets/screenshots/hq-13-SpamForDinner/step-2.png)

3. Enter the letters in the captcha in the text box below it and click *Make booking*
    - The website should refresh and add *Thanks, booking added* near the top of the form

![captcha](/assets/screenshots/hq-13-SpamForDinner/step-3.png)

![booking added](/assets/screenshots/hq-13-SpamForDinner/step-4.png)

4. Repeat the process 4 more times (for a total of 5 times)
    - Do not use the exact same *seedID* for each captcha or it will error!