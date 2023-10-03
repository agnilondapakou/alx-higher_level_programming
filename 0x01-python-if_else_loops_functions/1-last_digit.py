#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digi = int(repr(number)[-1])
if number < 0:
    last_digi = -last_digi
print(f"Last digit of {number} is {last_digi} and is ", end="")
if last_digi > 5:
    print("greater than 5")
elif last_digi == 0:
    print("0")
elif last_digi < 6 and last_digi != 0:
    print("less than 6 and not 0")
