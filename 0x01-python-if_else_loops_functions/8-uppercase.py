#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('A') <= ord(i) <= ord('Z'):
            i = chr(ord(i))
        print("{:s}".format(i), end='')
    print("")
