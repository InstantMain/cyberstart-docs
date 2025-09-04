# Perilous Pencils
Agent 707, we've just had an interesting piece of intel. It seems the gang know we're monitoring their own sites and servers, and have therefore started removing anything incriminating. But they still intend to implement their plans to steal the EMP and so need a new way of sharing information.

You may have already come across the pencil selling e-commerce site Kapa that the gang hacked into and have been using to exchange messages. The Spetzners, being geeky science types, do love their pencils, but we think it's a little more sinister than that - it seems they might have hacked the site and started adjusting the images on it to contain hidden messages! If we hadn't noticed them using the site, we would never have known. Clever.

Have a look at this page in particular which the gang member was looking at. Anything strange about it?

**Tip:** The flag is in one of the images! Oh, and for password protected files don't attempt to drag and drop them.

## Files
[challenge-pencilz-gioconda-01.de7c4fac.jpg](/assets/files/challenge-pencilz-gioconda-01.de7c4fac.jpg)  
[challenge-pencilz-gioconda-02.e76dd0ff.jpg](/assets/files/challenge-pencilz-gioconda-02.e76dd0ff.jpg)  
[challenge-pencilz-gioconda-03.d3dcf782.jpg](/assets/files/challenge-pencilz-gioconda-03.d3dcf782.jpg)

## Steps
1. Run *binwalk* to extract the zip file from *challenge-pencilz-gioconda-01.de7c4fac.jpg*
1. Change the other *.jpg* files to *.txt* files
1. Open both files and combine the words in the first line of the files to get the password of the extracted zip file (*Vidanya_Das*)

![second image text](/assets/screenshots/hq-10-PerilousPencils/step-1.png)

![third image text](/assets/screenshots/hq-10-PerilousPencils/step-1.1.png)

4. Unzip the zip file with the password
1. Execute the program in the unzipped folder in a Linux system