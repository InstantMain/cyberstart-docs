# Coffee Robot
An inside agent has told us Charlie Hampton, one of the gang's smartest engineers, has been making detailed notes, instructions and schematic drawings of the robot and keeping them on one of his servers. Getting access to those drawings would really help us understand how this robot will operate.

The problem is, we don't know which server he's keeping the plans on. All we do know is that Charlie owns a legit business, a coffee shop in East London, which he uses as a cover for his gang activities. It's a long shot but we do know they run a small server in the basement of the shop which controls their on-demand coffee ordering service. Go to the coffee ordering site, see if it's vulnerable. If it is see if you can find anything useful on the server.

**Tip:** Find the drawings file to get the flag.

## Steps
1. Bypass the text filter system in the *Your name* text box by entering *$(ls)* and click *Order drink*
    - Ignore *coffee-machine-service-info.txt* (does not contain the flag)

![list files](/assets/screenshots/hq-12-CoffeeRobot/step-1.png)

2. Enter in *$(ls ..)* in the text box and click *Order drink*
    - The flag is in the *robot-bank-job* directory (related to the notes of the robot)

![list directories](/assets/screenshots/hq-12-CoffeeRobot/step-2.png)

3. Enter in *$(ls ../robot-bank-job -a)* in the text box and click *Order drink*
    - Adding *-a* as a command argument lists all files, including hidden files

![list hidden files](/assets/screenshots/hq-12-CoffeeRobot/step-3.png)

4. Enter in *$(cat ../robot-bank-job/.robot_sketches.txt)* in the text box and click *Order drink*

![read robot drawings](/assets/screenshots/hq-12-CoffeeRobot/step-4.png)