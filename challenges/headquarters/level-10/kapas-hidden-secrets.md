# Kapa's Hidden Secrets
In what we thought was an unrelated piece of intel, one of our field agents monitoring the gang reported this morning that he noticed one of them looking at a site which sells pencils. Well, it seems they're using it for something else too - to hide files.

Luckily for us, we think the site is vulnerable to command injection. See if you can use the comment form to get access and find a file, we think it has a list of the gang members involved in the planned robbery and their particular role in the attack, so it's vital we get our hands on it right away.

## Steps
1. In the comment text box, add *$(ls)* and click *Add comment* to read the contents in the current directory

![ls command](/assets/screenshots/hq-10-Kapa'sHiddenSecrets/step-1.png)

2. Read the contents of the parent directory by adding *$(ls ..)* in the comment text box and click *Add comment*
    - There is a *flag.txt* in the parent directory

![ls .. command](/assets/screenshots/hq-10-Kapa'sHiddenSecrets/step-2.png)

3. Add *$(cat ../flag.txt)* in the comment text box and click *Add comment* to read the contents of the file

![read flag](/assets/screenshots/hq-10-Kapa'sHiddenSecrets/step-3.png)