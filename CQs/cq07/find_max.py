"""COMP 110 CQ#7"""

__author__ = "730524701"


def find_and_remove_max(list: list[int]) -> int:
    ## Return -1 if the list is empty
    if not list:
        return -1

    ## Create local variable to store the maximum value, just like EX04
    max = list[0]
    for i in list:
        if i > max:
            max = i

    while max in list:
        list.remove(max)

    return max
