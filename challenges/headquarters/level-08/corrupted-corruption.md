# Corrupted Corruption
Agent 707, there's another quick task I need your help with. One of the agents intercepted a zip file from The Chiquitoos, but it looks like it's corrupted. I know you've helped us with this kind of thing before. Can you take a look and see if you can get it working?

## Files
[masterkey-x86.zip](/assets/files/masterkey-x86.zip)

## Steps
1. Import the file in a hex editor

![imported file in hex editor](/assets/screenshots/hq-08-CorruptedCorruption/step-1.png)

2. Insert 4 bytes at the start with the values of *50 4B 03 04*

![inserted 4 bytes](/assets/screenshots/hq-08-CorruptedCorruption/step-2.png)

3. Export the file
1. Unzip the file and execute the program
    - Use *unzip* command to unzip it

![unzipped and executed file](/assets/screenshots/hq-08-CorruptedCorruption/step-3.png)