#!/usr/bin/python3
def safe_print_division(a, b):
    count = 0
    try:
        result = a / b
        count += 1
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
