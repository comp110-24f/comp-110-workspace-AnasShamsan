"""e"""

__author__ = "730524701"


def invert(input_dict: dict[str, str]) -> dict[str, str]:

    ## Create empty dict
    inverted_dict = {}

    ## Use for loop to go through the keys
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"KeyError: Duplicate key detected")
        ## Assign the key to the current value
        inverted_dict[value] = key

    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:

    ## Handle empty dictionary
    if not input_dict:
        return ""

    ## Create an empty dict to store count for each color
    color_value: dict[str, int] = {}

    ## First loop to store how many times each color appears
    for name, color in input_dict.items():
        if color in color_value:
            color_value[color] += 1
        else:
            color_value[color] = 0

    most_color = ""
    highest_color = 0

    for name, color in input_dict.items():
        if color_value[color] > highest_color:
            highest_color = color_value[color]
            most_color = color

    return most_color


def count(values: list[str]) -> dict[str, int]:

    ## Initialize an empty count
    counts: dict[str, int] = {}

    for item in values:
        ## Check if an item is already a key
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:

    values: dict[str, list[str]] = {}

    for word in words:
        ## Store the first letter of the word
        first_letter = word[0].lower()

        if first_letter in values:
            ## This line adds the word to the list
            values[first_letter].append(word)
        else:
            values[first_letter] = [word]
    return values


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:

    ## Check if the day is present
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]
