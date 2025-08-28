# Open Box
It looks like Billy Johnson, one of the gang's enforcers, is using a cloud storage service to keep his files secure. We know he has an account and we know his password, but we don't know his account name.

Our team have created an account with the service and logged in. See if you can find a way to trick the site into giving you a list of accounts.

**Tip:** Billy Johnson's account name is the flag.

## Steps
1. Go to *Cookies* in *Inspect*
    - Inspect > Application > Cookies > https://play.cyberstart.com

![application location](/assets/screenshots/hq-11-OpenBox/step-1.png)

![cookie location](/assets/screenshots/hq-11-OpenBox/step-2.png)

2. Append *‘ OR 1=1* to *SQL_SESSuser* cookie value (after the numbers)

![append sql injection](/assets/screenshots/hq-11-OpenBox/step-3.png)

3. Refresh the page
    - The flag is the account name attached to the name *Billy Johnson*

![admin page](/assets/screenshots/hq-11-OpenBox/step-4.png)