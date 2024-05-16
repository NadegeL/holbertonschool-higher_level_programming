#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element = 0
    try:
        for idx in range(x):
            if isinstance(my_list[idx], int):
                print("{:d}".format(my_list[idx]), end="")
                element += 1
    except (TypeError, ValueError):
       pass
    print()
    return element