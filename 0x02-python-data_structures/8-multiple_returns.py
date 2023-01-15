#!/usr/bin/python3


def multiple_returns(sentence):
    if (len(sentence) > 0):
        let = sentence[0]
    else:
        let = None
    return tuple((len(sentence), let))
