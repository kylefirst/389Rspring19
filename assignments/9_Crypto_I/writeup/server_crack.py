#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = [line.strip() for line in open("hashes.txt", "r")] # open and read hashes.txt
    passwords = [line.strip() for line in open("passwords.txt", "r")] # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337
    cracked = {}
    ctr = 0

    for c in characters:
        for p in passwords:
            text = c + p
            m = hashlib.sha256(text).hexdigest() # hash
            cracked[m] = text

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    # parse data
    # crack 3 times
    while(ctr < 3):
        # get hash from server
        data = s.recv(1024)
        m = data.split("\n")[2]

        print("-------------------------cracked hash---------------------------")
        print(m)
        print(cracked[m] + "\n")

        # send cracked text to server
        s.send(cracked[m] + "\n")

        ctr += 1
        time.sleep(1)

    # handle additional flag
    flag = s.recv(1024)
    print("flag: " + flag)

if __name__ == "__main__":
    server_crack()
