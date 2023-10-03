#!/usr/bin/python3
for counter in range(97, 123):
    if chr(counter) != 'q' and chr(counter) != 'e':
        print("{}".format(chr(counter)), end="")
