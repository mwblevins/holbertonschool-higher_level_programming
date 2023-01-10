#!/usr/bin/python3


def main():
    from sys import argv
    myarg = argv[1:]
    args = "arguments"
    if (len(myarg) == 1):
        args = "argument"
    period = "."
    if (len(myarg) > 0):
        period = ":"
    print("{0} {1}{2}".format(len(myarg), args, period))
    for x, y in enumerate(myarg, start=1):
        print("{0}: {1}".format(x, y))
if (__name__ == '__main__'):
    main()
