#!/usr/bin/python3
def no_c(my_string):
    # Remove all characters 'c' and 'C' from a string
    new_string = "".join([i for i in my_string if i != 'c' and i != 'C'])
    return new_string
