from typing import Union
from re import match
from sys import exit
from numpy import arange

NEW_GRID = ["Y", "N"]


class GridParser:

    def __init__(self, x: str, y: str, step: str):
        self.x = x
        self.y = y
        self.step = step

    def parse_grid(self):

        self.x = self._check_value(self.x, name="x coordinate axis")
        self.y = self._check_value(self.y, name="y coordinate axis")
        self.step = self._check_value(self.step, name="step")
        self.step = self._check_step(self.x, self.y, self.step)
        self._print_grid(self.x, self.y, self.step)

    @staticmethod
    def _check_value(value: str, name) -> Union[int, float]:
        while True:
            if not match(r"^\d+(\.\d+)?$", value):
                print(f"\nWrong value of {name}. Input value must be integer or decimal greater than 0 (zero).")
                value = input(f"Please enter valid {name} value: ")

            elif value.isdigit():
                value = int(value)
                return value

            else:
                value = float(value)
                return value

    @staticmethod
    def _check_step(x: Union[int, float], y: Union[int, float], step: Union[int, float]) -> Union[int, float]:
        while True:
            if not (step < x and step < y):
                print("\nStep value must not be greater or equal to x and y values.")
                step = input("Please enter valid step value: ")
                step = GridParser._check_value(step, name="step")

            elif not (x % step == 0 and y % step == 0):
                print("\nStep value should allow the division of both x and y without a remainder.")
                step = input("Please enter valid step value: ")
                step = GridParser._check_value(step, name="step")

            else:
                return step

    @staticmethod
    def _print_grid(x: Union[int, float], y: Union[int, float], step: Union[int, float]) -> None:
        grid = [[(i, j) for i in arange(0, x + step, step)] for j in arange(y, 0 - step, 0 - step)]
        print(*grid, sep='\n')


def new_grid(value: str) -> None:
    while True:
        if value.upper() == NEW_GRID[0]:
            print("\n\nGreat! Let's generate another grid.")
            break

        elif value == NEW_GRID[1]:
            print("\n\nThank you for using our program. Goodbye!")
            exit()

        else:
            print("\nWrong input.")
            value = input("Please enter 'Y' to make a new grid or 'N' for exit (register does not matter): ")


def main():
    print("This program generates grid in accordance with given boundary and step of the grid.\n")
    while True:
        grid = GridParser(input("Please enter the boundary value of x coordinate axis: "),
                          input("Please enter the boundary value of y coordinate axis: "),
                          input("Please enter the value of step: "))

        grid.parse_grid()

        print("\nWould you like to make a new grid? ")
        new_grid(input("Enter Y/N: "))


if __name__ == '__main__':
    main()
