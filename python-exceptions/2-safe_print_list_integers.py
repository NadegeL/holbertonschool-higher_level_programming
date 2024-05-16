#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element = 0
    try:
        for i in range(x):
            print("{:2}".format(my_list[i]), end="")
            element += 1
    except (TypeError, ValueError):
        continue
print("")
return printed
