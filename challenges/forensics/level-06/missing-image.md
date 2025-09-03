# Missing Image
Here's another file we intercepted a while back. We know it contains a secret, and we're pretty sure it's an image file. But for some reason, it doesn't seem to be detected as one. She has probably made a change to it in some way and our analysts were never able to figure out what.

**Tip:** Make the image work to get the flag.

## Files
[easter-island-02.jpg](/assets/files/easter-island-02.jpg)

## Steps
1. Download and import the image into a hex editor
1. Replace the first 3 bytes with the *.jpg* file signature header (*FF D8 FF*)

![replaced bytes](/assets/screenshots/fn-06-MissingImage/step-1.png)

3. Export the image as a *.jpg* file
1. Open the image

![flag text in image](/assets/screenshots/fn-06-MissingImage/step-2.png)