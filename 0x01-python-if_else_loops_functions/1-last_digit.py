#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digi = int(repr(number)[-1])
if last_digi > 5:
    print(f"Last digit of {number} is {last_digi} and is greater than 5")
elif last_digi == 0:
    print(f"Last digit of {number} is {last_digi} and is 0")
elif last_digi < 6 and last_digi != 0:
    print(f"Last digit of {number} is {last_digi} and is less than 6 and not 0")
