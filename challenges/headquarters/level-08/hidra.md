# Hidra
Well, this is interesting. We've finally been able to get access to a messaging app (called Hidra) that The Chiquitoo gang is using to communicate. Within an hour of looking at the messages, they've already given us some great intel.

For example, FTP login details to the gang's main server! One small issue: they mention the address and the username but not the password. See if you can find a way in.

**Tip:** Find the password for the user account. The flag is in a file which you get from connecting to the FTP server via a PASV connection. If you are inside the VM, you can use ftp -p.

## Files
[words.txt](/assets/files/words.txt)

## Steps
1. Brute force the login password for the given FTP server
    - Use *hydra* command

![brute force with hydra](/assets/screenshots/hq-08-Hidra/step-1.png)

2. Connect to the FTP server with the login details
    - Use *ftp* command on *services.cyberprotection.agency* with port *2121*

![connect to FTP server](/assets/screenshots/hq-08-Hidra/step-2.png)

3. Find the file containing the flag with the *ls* command

![find flag file with ls](/assets/screenshots/hq-08-Hidra/step-3.png)

4. Use *get* command to transfer *FLAG.txt* to your local computer

![transfer flag file](/assets/screenshots/hq-08-Hidra/step-4.png)

5. Open *FLAG.txt*

![open flag file](/assets/screenshots/hq-08-Hidra/step-5.png)