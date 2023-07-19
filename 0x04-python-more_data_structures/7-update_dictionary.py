#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    newItem = {key: value}
    a_dictionary.update(newItem)
    return a_dictionary
