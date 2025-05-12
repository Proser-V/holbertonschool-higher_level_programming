#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        firstchar = None
    else:
        firstchar = sentence[0]
    tuple_a = (len(sentence), firstchar)
    return tuple_a