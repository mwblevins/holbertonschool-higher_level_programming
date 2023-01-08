#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
str = ""
if number < 0:
    last = -last
if last == 0:
    str = ("0")
elif last < 5:
    str = ("less than 6 and not 0")
else:
    str = ("greater than 5")
print("Last digit of {} is {} and is {}".format(number, last, str))
