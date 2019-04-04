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

The hackers used port ```20``` (FTP-Data) to steal files from the server.

#### 5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,

    a) What kind of file is it?

    jpeg format image (find_me.jpeg)

    b) Where was this photo taken? Provide a city, state and the name of the building in your answer.

    The Hand, Rambla General Artigas, Punta Del Este, Maldonado, Uruguay

    c) When was this photo taken? Provide a timestamp in your answer.

    Sun, 23 December 2018 at 05:16:24 PM

    d) What kind of camera took this photo?

    Apple Iphone 8 (f/1.8 28mm focal length lens)

    e) How high up was this photo taken? Provide an answer in meters.

    4.5726 meters above sea level

#### 6. Which file did the attackers leave on the server?

```greetz.fpff```

#### 7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.

Use some firewall rule to only allow known IP addresses and require some encrypted authentication method like ```ssh``` to connect to the server.

### Part 2 (55 Pts)

1. Develop the parser, using both the
[specification](fpff-spec.md) and
`greetz.fpff` for reference. [stub.py](stub.py) contains the beginnings of a Python parser, if
you'd like to develop in Python.

My parser is called ```sol.py```. I manually parsed the Magic, Version, Header, Timestamp, Author and Section Count using ```Struct.unpack()``` with the corresponding bytes. Timestamp was in a weird format so I converted it to UTC time. Then I parsed to remaining bit of the file section by section. ```stype``` and ```slen``` were the first part of the section so I parsed those first. Then depending on ```stype``` I decided what to print out for results or file to save for pngs and gifs. Media files are written to a file as bytes with the data portion appended to the corresponding header type.

2. Parse `greetz.fpff`, and report the following information:
    1. When was `greetz.fpff` generated?

    - March 27th, 2019 at 4:15:05

    2. Who authored `greetz.fpff`?

    - fl1nch

    4. List each section, giving us the data in it *and* its type.

    | Section | Type | Length | Value |
    |---|---|---|---|
    | 1 | ASCII 0x1 | 24 | Hey you, keep looking :) |
    | 2 | COORD 0x6 | 0x6 | (52.336035, 4.880673) |
    | 3 | PNG 0x8 | 202776 | [Photo of Testudo](newPic.png) |
    | 4 | ASCII 0x1 | 44 | }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC |
    | 5 | ASCII 0x1 | 80 | Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30= |

    5. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.

    - CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}