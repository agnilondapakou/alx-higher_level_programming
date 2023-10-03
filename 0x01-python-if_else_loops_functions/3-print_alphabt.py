#!/usr/bin/python3
for counter in range(97, 123):
    if chr(counter) != 'e' and chr(counter) != 'q':
        print("{}".format(chr(counter)), end="")
