#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0

    for num in argv[1:]:
        sum = sum + int(num)
    print("{}".format(sum))
