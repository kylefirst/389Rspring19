# Writeup 6 - Forensics

Name: *Kyle Liu*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Kyle Liu*

## Assignment Writeup

### Part 1 (45 Pts)

#### 1. Warmup: what IP address has been attacked?

The attacked IP address is ```142.93.136.81``` (1337bank.money).

#### 2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

The attackers used SYN scanning on TCP using some kind of port scanning tool like ```nmap```.

#### 3. What are the hackers' IP addresses, and where are they connecting from?

The hackers ip address is ```159.203.113.181``` which corresponds to somewhere in *Clifton New Jersey, 07014*.

#### 4. What port are they using to steal files on the server?

The hackers used port ```20``` to steal files from the server.

#### 5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,

    a) What kind of file is it?

    jpeg format image (find_me.jpeg)

    b) Where was this photo taken? Provide a city, state and the name of the building in your answer.

    The Hand, Rambla General Artigas, Punta Del Este, Maldonado

    c) When was this photo taken? Provide a timestamp in your answer.

    Sun, 23 December 2018 at 05:16:24 PM

    d) What kind of camera took this photo?

    Apple Iphone 8 (f/1.8 28mm focal length lens)

    e) How high up was this photo taken? Provide an answer in meters.

    4.5726 meters above sea level

#### 6. Which file did the attackers leave on the server?

greetz.fpff

#### 7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.

Use some firewall rule to only allow known IP addresses and require some encrypted authentication method like ```ssh``` to connect to the server.

### Part 2 (55 Pts)

*Replace this text with your repsonse to our prompt for part 2!*
