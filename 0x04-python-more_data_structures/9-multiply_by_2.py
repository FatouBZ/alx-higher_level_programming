#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = a_dictionary.copy()
    for key in newDict.keys():
        newDict[key] = a_dictionary[key] * 2
    return newDict
