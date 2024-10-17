"""ex04 List Utility Functions"""

__author__ = "730524701"


def all(list: list[int], variable: int) -> bool:
    ##If list is empty
    if len(list) == 0:
        return False

    for i in list:
        if i != variable:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    ## Defind a local variable "largest" to store the max value
    largest = input[0]

    for i in input:
        if i > largest:
            largest = i
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    ## Check if lists are of the same length
    if len(list1) != len(list2):
        return False
    i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    i = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1
