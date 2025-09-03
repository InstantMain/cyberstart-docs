# Ancient Attachment
As part of investigating the ongoing communications between the dealers and hackers, we've been able to recover a mailbox file, extracted from a memory image by one of our analysts. Based on other messages we've seen we think there might be an attachment here with something interesting in it. See what you can find.

**Tip:** Open the attachment to get the flag.

## Files
[mailbox.pst](/assets/files/mailbox.pst)

## Steps
1. Download and open the file in a *PST* viewer
1. Download the *.zip* attachment from the message in the *Deleted Items* folder

![zip email](/assets/screenshots/fn-08-AncientAttachment/step-1.png)

3. Extract the *.zip* attachment with the password from the message in the *Notes* folder
    - The password is the Base64 text itself, not the decoded Base64 value

![password email](/assets/screenshots/fn-08-AncientAttachment/step-2.png)

4. Open the text file within the extracted folder