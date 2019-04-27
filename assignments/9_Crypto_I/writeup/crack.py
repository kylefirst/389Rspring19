#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = [line.strip() for line in open("hashes.txt", "r")] # open and read hashes.txt
    passwords = [line.strip() for line in open("passwords.txt", "r")] # open and read passwords.txt
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            # crack hashes
            text = c + p
            m = hashlib.sha256(text).hexdigest() # hash

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52
            if m in hashes:
                print(text + ":" + m)         

if __name__ == "__main__":
    crack()
