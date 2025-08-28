# Recruit List
Agent 707, the Spetzners are trying to recruit someone on the inside of the hidden weapons facility to help them get the access they need to steal the EMP. We believe one of the gang members has made a list of names of the people they want to target, and placed it on his own private web server.

We've found the login page for it, see if you can get access.

## Steps
1. View the page source code *(Ctrl + U)*
1. Find the comment in the source code talking about details on a certain page *(page.phps)*

![source code comment](/assets/screenshots/hq-09-RecruitList/step-1.png)

3. Go back to the website and change login to *page.phps* on the website URL
    - From the PHP code at the top, it is deduced that admin access is available if the *user* parameter, once decoded, equals *\<root>*

![PHP code](/assets/screenshots/hq-09-RecruitList/step-2.png)

4. Use online PHP compiler to urlencode *\<root>*
    - Results in *%3Croot%3E*

![PHP urlencode](/assets/screenshots/hq-09-RecruitList/step-3.png)

5. Manipulate the website link again and change *page.phps* to *login?user=%3Croot%3E*

![manipulated website link](/assets/screenshots/hq-09-RecruitList/step-4.png)

![web server access](/assets/screenshots/hq-09-RecruitList/step-5.png)