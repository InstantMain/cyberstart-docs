# Nightclub Rendezvous
Agent 707, we've been doing some research on Barry Brigley, one of the Bulldogs and a notorious art thief. We've managed to get access to a site he uses to post images of the art he's stolen which are for sale on the black market, but he's hiding the images somehow so we don't know what he's stolen. If we knew it would help us track his movements over the past few months (we think the art comes from a variety of galleries all over Europe).

Take a look at the site and the images. You can download the images, they're in a common image format, see if you can recover them.

**Tip:** The flag is in one of the images.

## Files
[artwork.11f7c21f](assets/files/artwork.11f7c21f)

## Steps
1. Download and import *artwork-03.jpg* into a hex editor

![imported in hex editor](/assets/screenshots/hq-11-ArtThief/step-1.png)
 
2. Add the jpg file signature header at the start *(FF D8 FF E0)*

![imported in hex editor](/assets/screenshots/hq-11-ArtThief/step-2.png)

3. Export the file as a *.jpg*
1. Open the image

![opened image](/assets/screenshots/hq-11-ArtThief/step-3.jpg)