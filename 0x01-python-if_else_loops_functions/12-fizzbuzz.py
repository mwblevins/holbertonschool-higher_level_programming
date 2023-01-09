#!/usr/bin/python3


def fizzbuzz():
    ourprint = ""
    for x in range(1, 101):
        ourprint = ""
        if (x % 3 == 0):
            ourprint += "Fizz"
        if (x % 5 == 0):
            ourprint += "Buzz"
        if (ourprint == ""):
            ourprint = "{}".format(x)
        print(ourprint.format(), end=" ")
