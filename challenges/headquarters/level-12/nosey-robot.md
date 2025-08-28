# Nosey Robot
Agent 707, thanks to your efforts in finding the gang member leading the effort to send a robot to the bank, we've managed to recover some C code we think might be used by the robot to take photos, but we can't be sure because running it currently returns a segmentation fault. Another agent has rigged up the code to a camera interface. See if you can fix the code, get it to run and take a photo.

## Original Code
```c
#include <stdio.h>
#include <string.h>

int main()
{
  int take_photo = 0;
  char command[8];
  char *pictures = "take_pictures";
  strcpy(command, pictures);

  if (strcmp(command, "take_pictures") == 0) {
    printf("%s\n", "CLICK_PHOTO_TAKEN");
    take_photo = 1;
  } else {
    printf("%s\n", "SEG_FAULT_NO_PHOTO");
  }
  return 0;
}
```

## Steps
1. Change *command[8]* to *command[13]*

```c
#include <stdio.h>
#include <string.h>

int main()
{
  int take_photo = 0;
  char command[13];
  char *pictures = "take_pictures";
  strcpy(command, pictures);

  if (strcmp(command, "take_pictures") == 0) {
    printf("%s\n", "CLICK_PHOTO_TAKEN");
    take_photo = 1;
  } else {
    printf("%s\n", "SEG_FAULT_NO_PHOTO");
  }
  return 0;
}
```