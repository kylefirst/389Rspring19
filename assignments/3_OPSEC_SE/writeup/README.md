# Writeup 3 - Operational Security and Social Engineering

Name: *Kyle Liu*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Kyle Liu*

## Assignment Writeup

### Part 1 (40 pts)

Because Elizabeth currently works as a high-ranking executive at a bank, I would call her posing as a bank employee with an urgent notice that her account has been breached and requires her to verify some personal info and follow some steps to protect her account. Before diving into the Q&A, I would build rapport with a backstory about my fake identity as a fellow Dutch citizen. After explaining the scope of the break, I would ask her a few questions to verify her identity to proceed with the more sensitive steps. The city she was born in, name of her first pet, and her mother's maiden name are all commonly used questions for account security, so asking her to answer these questions for verification purposes should not raise any red flags. If she would get suspicious through this process, I would mention my position at the company she works for and some of the employee's she knows at the company, and her username v01dcache from social accounts to reduce suspicion. After verifying her identity, I would direct her to a fake key logged bank webpage to gather her browser and ATM pin number. Before she navigates to the site I would ask what browser she primarily uses to ensure compatibility. Then I would ask her to login to the site with her atm pin number to verify that her banking info is correct. After retrieving all this information, I would not end the right away because this would raise suspicions. I would talk her through the process of navigating the webpage further and then end the call to “investigate further” once she reaches an error screen.

### Part 2 (60 pts)

1. **Weak Passwords** are currently an issue with 1337Bank's webserver because we were able to easily brute force the password using a common wordlist. The current password was easily cracked because it is a commonly used short alpha string. In order to make the password more secure, 1337Bank should at least follow the [NIST guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html) on strong passwords. These guidelines recommend users use passwords that are at least 8 digits long, uncommon word or phrases that do not exist in a wordlist or a previous breach and a mix of alpha-numeric characters and symbols (123abc!@#).

2. **Open Ports** are also currently an issue with 1337Bank's server. We could fix this issue by closing all ports not needed (garbage ports) and blacklisting any IP addresses that spike network traffic too much using a firewall or other network security tool. This is effective because we learned that Nmap scans are very noisy during class. A Nmap scan on all ports will cause a big spike in network traffic that is easily traceable and detectable by the server admin. If an attacker does not have any open ports to use to brute force the server, cracking the server will be much harder.

3. **Unsecured Login** is another issue with 1337Bank's web server. We were able to send unencrypted text passwords to login to the server last project. A [MITM Attack](https://us.norton.com/internetsecurity-wifi-what-is-a-man-in-the-middle-attack.html) listening to all traffic connected to 1337Bank's webserver could intercept these usernames and passwords and use them to login to the server. To solve this issue, we could use require SSH to login to the server. This way, all identifiable information sent (username, passwords, etc) are encrypted and an attacker would have a hard time decrypting information even after a successful MITM attack.
