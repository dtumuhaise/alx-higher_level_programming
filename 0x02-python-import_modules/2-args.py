#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    i = 1

    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))

    for x in argv[1:]:
        print("{}: {}".format(i, x))
        i += 1
