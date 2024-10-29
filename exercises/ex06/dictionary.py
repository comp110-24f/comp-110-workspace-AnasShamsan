"""e"""

__author__ = "730524701"


def invert(input_dict: dict[str, str]) -> dict[str, str]:

    inverted_dict = {}

    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"KeyError: Duplicate key detected")

        inverted_dict[value] = key

    return inverted_dict
