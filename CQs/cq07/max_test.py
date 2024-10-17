"""COMP 110 CQ#7"""

__author__ = "730524701"


from CQs.cq07.find_max import find_and_remove_max


def test_1() -> None:
    result = find_and_remove_max([1, 2, 3, 4])
    assert result == 5


def test_2() -> None:
    b = [1, 2, 3, 4]
    find_and_remove_max(b)
    assert b == [1, 2, 3]


def test_3() -> None:
    c = [-1, 0, 1, 2]
    find_and_remove_max(c)
    assert c == [-1, 0, 1]
