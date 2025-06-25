#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size):
        """Initializes the square with a specific size."""
        self._Square__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
