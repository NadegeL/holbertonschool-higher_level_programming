#!/usr/bin/python3
def safe_print_integer(value):
    for i in range(1):
        try:
            print("{:d}".format(value))
            return True
        except ValueError:
            return False
