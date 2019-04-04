#!/usr/bin/env python2

import sys
import struct
import base64
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
timestamp = datetime.datetime.utcfromtimestamp(int(struct.unpack("<L", data[8:12])[0])).isoformat()
author = ''.join(struct.unpack("<8s", data[12:20]))
section_count = int(struct.unpack("<L", data[20:24])[0])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % timestamp)
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % section_count)

print("-------  BODY  -------")

# Section Types
SECTION_ASCII = 0x1
SECTION_UTF8 = 0x2
SECTION_WORDS = 0x3
SECTION_DWORDS = 0x4
SECTION_DOUBLES = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_PNG = 0x8
SECTION_GIF87 = 0x9
SECTION_GIF89 = 0xA

body = data[24:]
pos = 0

# Parse Body
for section in range(1,section_count+1):
    stype = hex(struct.unpack("<L", body[pos:(pos+4)])[0])
    slen = int(struct.unpack("<L", body[(pos+4):pos+8])[0])
    pos = pos+8

    # Display Metadata
    print("SECTION: %d" % (section))
    print("TYPE: %s" % stype)
    print("LENGTH: %d" % slen)

    # Display Value
    if stype == hex(SECTION_ASCII):
        print("VALUE: %s\n" % (struct.unpack(("<%ds" % slen), body[(pos):(pos+slen)]))[0])

    elif stype == hex(SECTION_UTF8):
        print("  VALUE: %s\n" % (struct.unpack(("<%ds" % slen), body[(pos):(pos+slen)])).decode('utf-8')[0])

    elif stype == hex(SECTION_WORDS):
        words = slen / 4
        print("  VALUE: %s\n" % (struct.unpack(("<%s" % 'L'*words), body[(pos):(pos+slen)]))[0])

    elif stype == hex(SECTION_DWORDS):
        dwords = slen / 8
        print("  VALUE: %s\n" % (struct.unpack(("<%s" % 'Q'*dwords), body[(pos):(pos+slen)]))[0])

    elif stype == hex(SECTION_DOUBLES):
        doubles = slen / 8
        print("  VALUE: %s\n" % (struct.unpack(("<%s" % 'd'*doubles), body[(pos):(pos+slen)]))[0])

    elif stype == hex(SECTION_COORD):
        print("COORDINATES: %s\n" % (struct.unpack("<dd", body[(pos):(pos+slen)]),))

    elif stype == hex(SECTION_REFERENCE):
        print("REFERENCE: %d\n" % int(struct.unpack("<L", body[(pos):(pos+slen)])[0]))

    # Write Image/Gif as byte arrays
    elif stype == hex(SECTION_PNG):
        signature = [137, 80, 78, 71, 13, 10, 26, 10]

        newPic = open("newPic.png", "wb")
        newPic.write(bytearray(signature + list(struct.unpack('<' + ("%s" % 'B'*slen), body[(pos):(pos+slen)]))))

        print("\n")

    elif stype == hex(SECTION_GIF87):
        signature = [47, 49, 46, 38, 37, 61]
       
        newGif = open("newGif87.gif", "wb")
        newGif.write(bytearray(signature + list(struct.unpack('<' + ("%s" % 'B'*slen), body[(pos):(pos+slen)]))))

        print("\n")

    elif stype == hex(SECTION_GIF89):
        signature = [47, 49, 46, 38, 39, 61]

        newGif = open("newGif89.gif", "wb")
        newGif.write(bytearray(signature + list(struct.unpack('<' + ("%s" % 'B'*slen), body[(pos):(pos+slen)]))))

        print("\n")
    
    pos = pos + slen