#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
    print(best_key)