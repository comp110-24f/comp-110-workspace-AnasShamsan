"""COMP 110 CQ#2"""

__author__ = "730524701"


def guess_a_number() -> None:

    secret = int(7)
    guess = int(input("Guess a number: "))

    print("Your guess was " + str(guess))

    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
