#!/usr/bin/python3


def uppercase(str):
    cap = ord('A') - ord('a')
    lis = list(str)
    for x, y in enumerate(str):
        if (ord(y) in range(ord('a'), ord('z')+1)):
            lis[x] = chr(ord(y) + cap)
        print("".join(lis).format())
