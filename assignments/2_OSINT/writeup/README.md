# Writeup 2 - OSINT

Name: *Kyle Liu*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Kyle Liu*

## Assignment Writeup

### Part 1 (45 pts)

1. Elizabeth Moffet
2. Banking CEO at 13/37 National Bank (http://1337bank.money)
3. See table below

|Type|Username/Link| Discovery Method |
|---|---|---|
|Pastebin (v0idcache/fl1nch Chat Logs)|https://pastebin.com/WghDuAr7|Google Search
| Github (no public activity) | https://github.com/v0idcache | Github search by user
| Twitter handle| [@v0idcache](https://twitter.com/v0idcache?lang=en) | Twitter Advanced Search
| Activity with other Twitter users | [@CacheDev0id](https://twitter.com/CacheDev0id?lang=en) | Twitter Advanced Search 
| Twitter following | [@umdcsec](https://twitter.com/umdcsec?lang=en) | Twitter Bio
| Location | Netherlands | Twitter Bio |
| Email | v0idcache@protonmail.com | About section of bank webpage |
4. See table below

| IP Address | Host/Location | Discovery Method |
|---|---|---|
| 142.93.136.81 | Digital Ocean/Canada| Reverse DNS lookup (dnsdumpster.com) 
| 162.255.118.61/162.255.118.62 | Namecheap (Email)/United States | Reverse DNS lookup (dnsdumpster.com) 
| 216.87.155.33 | Verisign Certificate (Namecheap)/United States | Reverse DNS lookup (dnsdumpster.com)
5. See table below

| Website Flags | Discovery Method |
|---|---|
| CMSC389R-{h1dd3n_1n_plain_5ight} | inspect element |
| CMSC389R-{h1ding_fil3s_in_r0bots_L0L} | robots.txt |
6. nmap scan of first 10000 ports

```
22/tcp   open     ssh
25/tcp   filtered smtp
80/tcp   open     http
554/tcp  open     rtsp
1337/tcp open     waste
7070/tcp open     realserver
```

7. OS is most likely some version of linux accoring to nmap -O
```
Aggressive OS guesses: Linux 4.4 (91%), Linux 4.0 (87%), Linux 3.11 - 4.1 (87%), Cisco RV320 router (87%), Linux 2.6.32 (87%), Linux 2.6.32 or 3.10 (87%), Linux 3.10 - 3.12 (86%), Dish Network Hopper media device (86%), Linux 3.16 (85%), Linux 2.6.32 - 3.0 (85%)
```
8. See table below

| Bonus Flags | Discovery Method |
|---|---|
| CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}| DNS Records |
| CMSC389R-{brut3_f0rce_m4ster} | Brute forcing server |
| CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh} | AB4300.txt file from pastebin in server|

### Part 2 (75 pts)

Working bruteforce program is called ```sol.py```

I have a loop that sends all the passwords in the wordlist (rockyou.txt file in kali) one at a time for v0idcache's user account to the server on the open port until the response from the server told me the username/password combination is valid. I formatted the payload to send for the username and password using struct.pack() in a char[] string format and then sent to payload to the server using s.send().