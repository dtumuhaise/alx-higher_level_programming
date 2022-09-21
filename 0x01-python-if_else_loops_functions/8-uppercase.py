#!/usr/bin/python3
def uppercase(str):
    output = ''
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            output += chr(ord(ch) - 32)
        else:
            output += ch
    print("{:s}".format(output))
