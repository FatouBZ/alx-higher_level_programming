#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    a = 0
    display = 0
    for a in range(0, x):
        try:
            print("{}".format(my_list[a]), end="")
            display += 1
        except:
            continue
    print()
    return display
