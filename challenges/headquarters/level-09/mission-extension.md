# Mission Extension
Agent, those Spetzners are really trying to test our patience! We have someone on the inside that managed to quickly take a copy of one of the gang's hard drives. But just to make it really hard to figure out what they're doing they've removed all file extensions - from every file!

We know there's a Jpeg in there somewhere with an image of the particular EMP they're trying to steal, but it's taking the team forever to find it. Can you think of a quicker way?

- Username: *[given username]*
- Password: *[given password]*
- IP Address: *[given ip]*
- Port: *[given port]*

**Tip:** Find the Jpeg, it contains a serial number (SN), that's the flag!

## Steps
1. Log into the SSH account
    - Use *ssh* command

![ssh](/assets/screenshots/hq-09-MissionExtension/step-1.png)

2. Use *ls* command and go into *Contents* using the *cd* command

![go into Contents](/assets/screenshots/hq-09-MissionExtension/step-2.png)

3. Use *file \** command to locate the JPEG file

![file command](/assets/screenshots/hq-09-MissionExtension/step-3.png)

![found JPEG file](/assets/screenshots/hq-09-MissionExtension/step-3.1.png)

4. Log out of the account
    - Exit out of terminal and relaunch it
1. Copy the JPEG file from the remote computer to the local computer
    - Use *scp* command

![transfer file](/assets/screenshots/hq-09-MissionExtension/step-4.png)

6. Open the file
    - The characters after *SN*: is the flag

![opened file](/assets/screenshots/hq-09-MissionExtension/step-5.png)