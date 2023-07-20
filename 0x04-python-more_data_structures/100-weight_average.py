#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num1 = 0
    num2 = 0
    for i in my_list:
        num1 += (i[0] * i[1])
        num2 += i[1]
        return num1 / num2
