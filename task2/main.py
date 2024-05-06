""" import regex, typing """
import re
from typing import Callable, Generator


def generator_numbers(data) -> Generator[float, None, None]:
    """ get numbers from string data """
    for match in re.finditer(r'\d*\.?\d+', data):
        # return number and save state
        yield float(match.group())


def sum_profit(data: str, pool_create: Callable) -> int:
    """ calculate sum of all numbers on text """
    pool = pool_create(data)
    # calculate
    result = sum(pool)
    return result


def main():
    """ main function """
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()
