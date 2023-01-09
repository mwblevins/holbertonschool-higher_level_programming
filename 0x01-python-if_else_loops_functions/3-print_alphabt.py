#!/usr/bin/python3


for x in range(ord('a'), ord('z')+1):
    if (x != ord('e') and x != ord('q')):
        print(chr(x).format(), end="")
