"""CQ4 Coordinates"""

__author__ = "730524701"


def get_coords(xs: str, ys: str) -> None:
    idx = 0
    while idx < len(xs):
        jdx = 0
        while jdx < len(ys):
            print(f"({xs[idx]},{ys[jdx]})")
            jdx += 1
        idx += 1
