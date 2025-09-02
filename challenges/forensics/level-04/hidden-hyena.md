# Hidden Hyena
Our team in Kenya decided to take a page out of the hackers playbook and try sending an agent of their own along on one of the tours to follow a suspect they suspected might be one of the hackers. Our agent noticed them using a particular website which we believe had a secret message on it for him. Take a look at the network capture file and see if you can find anything interesting.

**Tip:** The flag is in the pcap.

## Files
[Tour Capture.pcapng](</assets/files/Tour Capture.pcapng>)

## Steps
1. Download and open the *.pcapng* file in *WireShark*
1. Search for the packet near the bottom with Info *HTTP/1.1 200 OK (text/html)* and includes *\<h1>Hello Again Agent\</h1>\n* as the text data
    - Display filter can be used (*Ctrl + F*), input *data-text-lines && http.response.code == 200*, and click *Find*

![target packet](/assets/screenshots/fn-04-HiddenHyena/step-1.png)

3. Drop down the details for *Hypertext Transfer Protocol*

![HTTP details](/assets/screenshots/fn-04-HiddenHyena/step-2.png)

4. At *Request URI*, copy the *.html* name from *evilthingshere.net*

![HTTP name](/assets/screenshots/fn-04-HiddenHyena/step-3.png)

5. *Base64* decode the text

![name decoded](/assets/screenshots/fn-04-HiddenHyena/step-4.png)