"""Tea party program to calculate # of tea bags, treats, and cost"""

__author__ = "730524701"


def main_planner(guests: int) -> None:
    """Main planner for tea party"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  ## Intro statement, b/c it's not return, then str() inside print
    print("Tea Bags: " + str(tea_bags(people=guests)))  ## Tea bags count
    print("Treats: " + str(treats(people=guests)))  ##  Treats count
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  ## Now group everything together to calc the cost


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost needed for the party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
