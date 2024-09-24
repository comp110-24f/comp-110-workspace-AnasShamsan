"""COMP 110 CQ#3"""

__author__ = "730524701"


## Write function signature line
def num_instances(phrase: str, search_char: str) -> int:

    ## Initialize count and index, set them to zero
    count: int = 0
    index: int = 0

    while index < len(phrase):
        ##Check characters of phrase
        if phrase[index] == search_char:
            count += 1
        ##Add 1 to move to next character, then force loop to quit
        index += 1

    return count
