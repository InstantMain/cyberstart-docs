# Brazilian Blather
Another bit of evidence you can take a look into, Agent 707 - a packet capture containing an email conversation and attachments from some interactions the hacker had with a gang member in Brazil. Do some analysis and see what you come up with.

**Tip:** Answer the question to get the flag.

## Files
[Email_Capture_3.pcapng](/assets/files/Email_Capture_3.pcapng)

## Steps
1. Download and import the *.pcapng* file into *Wireshark*
1. Filter for packets using the *POP* protocol
1. Right click any packet and select *Follow > TCP Stream*

![second image text](/assets/screenshots/fn-06-BrazilianBlather/step-1.png)

4. Change *Show as* to *ASCII*
1. Scroll to near the bottom and find the question
    - *This is what we found, question is: What year did AMD release the K6 Processor?*

![second image text](/assets/screenshots/fn-06-BrazilianBlather/step-2.png)

6. Google the answer to this question (*1997*)
1. Scroll further down and copy the *Base64* text
1. Decode and export the Base64 into a *gzip* file
1. Unzip the file and run the executable inside
1. Use the answer to the question as the program input