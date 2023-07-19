#!/usr/bin/python3
def uniq_add(my_list=[]):
    List = set(my_list)
    num = 0
    for i in List:
        num += i
    return num
