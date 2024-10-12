"""ex03 wordle"""

__author__ = "730524701"


### Prompt user to input word
def input_guess(secret_word_len: int) -> str:
    while True:
        guess = input(f"Enter a {secret_word_len} character word: ")
        if len(guess) == secret_word_len:
            return guess
        else:
            print(f"That wasn't 5 chars! Try again: ")


### Check if secret word contains guessed letter
def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    i = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i += 1
    return False


### Define new variables for emojis

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


### Emjoifi the result
def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    result = ""
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX  ## Definitly make sure to outdent the code properly to avoid mistakes
        elif contains_char(
            secret, guess[i]
        ):  ## Now it makes sense how to link the previous function
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


### Defind main function
def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turns = 1
    max_turns = 6
    won = False

    while turns <= max_turns and not won:  ## Good idea to use negation,

        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))
        emoji = emojified(guess, secret)
        print(emoji)

        if guess == secret:
            won = True
        else:
            turns += 1

    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
