# Cryptonite
Yesterday our uncover agent let us know about an encryption tool one of the gang built called Cryptonite. It runs on one of the Bulldogs private servers and we think it might be vulnerable.

See if you can use it to get access to the server and look for any files that might be worth investigating. We think the gang member who built it, Percy Pinkly, is involved in the gangs efforts to circumvent the banks main security alarms, so he might have been storing files on the server related to blueprints or the security system.

## Steps
1. Enter in *cryptonite -h* and click *Enter* to show its arguments
    - *cryptonite -n* can be used to ignore the command and used for command injection

![see valid arguments](/assets/screenshots/hq-11-Cryptonite/step-1.png)

2. Enter in *cryptonite -n; ls* and click *Enter*
    - In the current directory, there is a *.txt* file with its name related to blueprints and security

![see list of files](/assets/screenshots/hq-11-Cryptonite/step-2.png)

3. Enter in *cryptonite -n; cat security-blueprints.txt* and click *Enter*

![look into blueprints](/assets/screenshots/hq-11-Cryptonite/step-3.png)