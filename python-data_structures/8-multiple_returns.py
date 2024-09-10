#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)
#on calcule d'abord la longueur puis on retourne le premier caractère de la phrase