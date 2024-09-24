"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730524701"


## Defind the function that will prompt user to input a word
def input_word() -> str:
    word = input("Enter a 5-character word: ")

    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


## Defind the function that will prompt user to input a letter
def input_letter() -> str:
    letter = input("Enter a single character: ")

    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()  ## Exit the program if not single letter


def contains_char(word: str, letter: str) -> None:
    print(f"Searching for {letter} in {word}")

    ## Local variable match count to iterate through each letter and count instances
    match_count = 0

    ## Check if the both conditions for word and letter check
    if len(word) == 5 and len(letter) == 1:

        ## Manually go through each letter word[index]
        if word[0] == letter:
            print(f"{letter} found at index 0")
            match_count += 1
        if word[1] == letter:
            print(f"{letter} found at index 1")
            match_count += 1
        if word[2] == letter:
            print(f"{letter} found at index 2")
            match_count += 1
        if word[3] == letter:
            print(f"{letter} found at index 3")
            match_count += 1
        if word[4] == letter:
            print(f"{letter} found at index 4")
            match_count += 1

        if match_count == 0:
            print(f"No instances of {letter} found in {word}")
        elif match_count == 1:
            print(f"1 instance of {letter} found in {word}")
        else:
            print(f"{match_count} instances of {letter} found in {word}")


## Defind a main function to put the functions together
def main() -> None:
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)


## Run the program
if __name__ == "__main__":
    main()
