# Multiple Boxes
Could this be the icing on the cake? Remember Filebox, the cloud storage site Bulldog gang member Billy Johnson was using to store his files? Well, it seems he's not the only gang member to store his secret files there.

As we know it's vulnerable we want to look at other ways to find the gang's files. We think the files can be exposed with directory traversal and there are some two levels up from the account page. See if you can get access to them.

## Steps
1. Add */..%2F..%2F..%2F..%2F..%2F..%2F* in the URL link after */files*
    - *%2F* is the hexadecimal form of */*

![path traversal attack](/assets/screenshots/hq-12-MultipleBoxes.png)