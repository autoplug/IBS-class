
from random import random
from types import EllipsisType


class BreakException(Exception):
    pass


class MoreThan(Exception):
    pass


class LessThan(Exception):
    pass


mynumber = 42
your_guess = 1

while True:
    print(f"your guess = {your_guess}")
    try:
        if your_guess == mynumber:
            raise BreakException
        elif your_guess > mynumber:
            raise MoreThan
        else:
            raise LessThan

    except BreakException:
        print("guess true")
        break
    except MoreThan:
        pass
    except LessThan:
        pass
