#!/usr/bin/python3

def multiple_returns(sentence):

    res = tuple(sentence)

    if len(res) == 0:
        res[0] = None
    else:
        return len(res), res[0]
