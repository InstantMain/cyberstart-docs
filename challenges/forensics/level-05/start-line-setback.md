# Start Line Setback
Well, that wasn't a promising start. On our very first review, we found an image file on one of the company's servers which doesn't look quite right. We think whoever left it there has used a tool to add a passphrase to it and hide something inside. Take a look and see what you think.

**Tip:** Open the file to find the flag.

## Files
[runner.jpg](/assets/files/runner.jpg)

## Steps
1. Download the image on the page
1. Import the image into a hex editor
1. Scroll to the very bottom of the hex editor to find the password for steganography decoding

![steganography password](/assets/screenshots/fn-05-StartLineSetback/step-1.png)

4. Extract the files from the image with the password
    - The password is *givemetheflag* as shown in the hex editor

![imported file](/assets/screenshots/fn-05-StartLineSetback/step-2.png)

![hidden text file](/assets/screenshots/fn-05-StartLineSetback/step-3.png)