# Dodgy Dealers
To help expand the investigation we've been permitted to do some analysis on the machines of other dealers that weren't under suspicion of being involved, and we've already found something interesting. Take a look at this network capture, an initial analysis has revealed that it might have some hidden messages in it, can you help us figure out what they are?

**Tip:** The flag is in the message.

## Files
[wraw.pcapng](/assets/files/wraw.pcapng)

## Steps
1. Download and open the file in *Wireshark*
1. Right click any of the *TCP* packets and select *Follow > TCP Stream*

![TCP Stream selection](/assets/screenshots/fn-08-DodgyDealers/step-1.png)

3. Change *Show as* to *Raw*

![raw data](/assets/screenshots/fn-08-DodgyDealers/step-2.png)

4. Save the data as a *.wav* file
1. Open the audio file
    - "The flag is the *MD5* value of the word *wireshark* all lowercase."

![MD5 hash](/assets/screenshots/fn-08-DodgyDealers/step-3.png)