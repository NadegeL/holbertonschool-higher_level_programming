#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_list = 0
    unique_number = []
    for num in my_list:
        if num not in unique_number:
            sum_list += num
            unique_number.append(num)
    return sum_list
