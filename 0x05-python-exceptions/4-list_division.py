#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    takes two lists and creates a new list with result of divison
    operation

    handles errors and prints them to stdout
    """
    a = 0
    new_list = []
    answer = 0
    for i in range(0, list_length):
        try:
            answer = (my_list_1[a] / my_list_2[a])
        except TypeError:
            answer = 0
            print("wrong type")
        except ZeroDivisionError:
            answer = 0
            print("division by 0")
        except IndexError:
            answer = 0
            print("out of range")
        finally:
            new_list.append(answer)
    return new_list
