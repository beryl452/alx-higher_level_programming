#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        character = None
    else:
        character = sentence[0]
    my_tuple = (lenght, character)
    return my_tuple
