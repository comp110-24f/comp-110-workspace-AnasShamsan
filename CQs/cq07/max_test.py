"""COMP 110 CQ#7"""

__author__ = "730524701"


from CQs.cq07.find_max import find_and_remove_max

a: list[int] = [1, 2, 3, 4]
result = find_and_remove_max(a)

b: list[int] = [1, 2, 3, 4]
find_and_remove_max(b)

c: list[int] = [-1, -2, 0]
find_and_remove_max(c)
