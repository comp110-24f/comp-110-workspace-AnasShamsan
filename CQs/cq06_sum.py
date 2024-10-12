"""Summing the elements of a list using different loops"""

__author__ = "730524701"


def w_sum(vals: list[float]) -> float:
    i = 0
    value: float = 0.0
    while i < len(vals):
        value += vals[i]
        i += 1
    return value


def f_sum(vals: list[float]) -> float:
    value: float = 0
    for i in vals:
        value += i
    return value


def f_range_sum(vals: list[float]) -> float:
    value: float = 0
    for i in range(len(vals)):
        value += vals[i]
    return value
