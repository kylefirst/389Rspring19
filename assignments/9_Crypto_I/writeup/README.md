# Crypto I Writeup

Name: *Kyle Liu*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Kyle Liu*

## Assignment Writeup

### Part 1 (70 Pts)
```
python crack.py 
afreedom:52e5a82e5763533be232e82482d3e6f44118f88b1b6bd3224134341979fe43cc
apassword:739145a8634b184276559a2f3055353db3b261109649ef78445149415f0b4dee
b1234567890:f3a885dd12d13ad8e58b5f6c10730a720f61103f651dfb0f49670bad8c7305d5
gwestside:518499174f0754eaf5421fdc17499bc8865b4c6419fbf616f17d38eb741073aa
nsuperman:7e4096245b7ce7689e665c9054d612c1894ad0d182b60b5a9be1c8b10e817306
owhatever:833c3b30b541406a644932cd498fb4d85c65f11e4968333be659c31812d2d6be
qnicole:dbec1495345f5a1573a0dd437c207cacc844f74b8a7b030c858f4f660bf9484f
tshadow:3f6c2527aa5f8eb3ae4bd5b33d772ba819196a95f09ad430c67c3b5b9570711e
uwelcome:3d925228586369644c84ae5da6753faf8109db1f725c60ccb6dffb914797d289
zmatrix:247ead31de7efd5c8fd859630ecb959c4e6240646fcd4d41962f25b1fb33c702
```

### Part 2 (30 Pts)
I computed the hashes for all the passwords and stored them in a map to match the server outputs to in order to find the corresponding input character + password. 
```
$ python server_crack.py 
-------------------------cracked hash---------------------------
4b742aa9417fc093fa7fc0fe1b4279976afe483354f26483d263c1174bf46974
yblahblah

-------------------------cracked hash---------------------------
6c21eb0e46a4bf58943fdebd6eab6bb4adfc13b2958ed8f0bfbe0603f424aa8f
vasdfasdf

-------------------------cracked hash---------------------------
b25a3021db2a916dc2d7ada0b3000c5bb42b657222f74c596ff3a5fe94eabcf6
kasdfasdf

flag: CMSC389R-{h@sh1ng_@nd_sl@sh1ng}
```