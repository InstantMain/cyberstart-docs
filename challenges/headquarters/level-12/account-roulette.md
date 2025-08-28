# Account Roulette
Agent 707, remember the social media website from the previous level where Bulldog gang member Darren Greggs posted that cryptic message? If we could log in as Darren we could post messages as him and confuse other gang members. Unfortunately we don't have his login details, but we're sure you can find another way to log in as him using a possible vulnerability we think exists.

We have logged in as a random test user that we created and have gone to an old message Darren posted. See if you can use that access to log in to other accounts, then check the response to see who you are logged in as, aiming to find access Darren's account (his username is thedazman).

## Steps
1. Write Python code

![python to cookie login](/assets/screenshots/hq-12-AccountRoulette/step-1.png)

2. Copy the number in the output and go into *Cookies* using *Inspect*
    - Inspect > Application > Cookies > https://play.cyberstart.com

![application location](/assets/screenshots/hq-12-AccountRoulette/step-2.png)

3. Replace *speek_sess_id* cookie value with the copied number

![replace speek_sess_id](/assets/screenshots/hq-12-AccountRoulette/step-3.png)

4. Refresh the page