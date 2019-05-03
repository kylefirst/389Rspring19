# Crypto II Writeup

Name: *Kyle Liu*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Kyle Liu*

## Assignment Writeup

### Part 1 (70 Pts)

I loaded the secret key with gpg by running ```gpg --import key.asc``` and decrypted the file by running ```gpg --decrypt message.txt.gpg```.

I found the flag ```CMSC389R-{m3ss@g3_!n_A_b0ttl3}``` in the document.

![secret-keys](secret-keys.png)

The cleartext signature I got by running ```gpg --cleartext signature.txt``` is in the writeup folder.

### Part 2 (30 Pts)

![original](original.bmp)
![ecb](ecb.bmp)
![cbc](cbc.bmp)

1. The shapes in the oriinal image are present in the second image encrypted with ecb. You cannot distinguish the original image from the noise in the third image encrypted with cbc.

2. ecb is less secure than cbc. From the results in the image, we see that ecb does not completely obfuscate the image while cbc does. Encrypting the same block of text will with ecb will result in the same predictable cipher text block while encrypting a block of text with cbc has much more variability because it XORs different blocks and an independent Intialization Vector.