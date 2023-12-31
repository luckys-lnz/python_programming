#!/usr/bin/python3

""" Class that defines a square """
class Square:
    """
    A square class with a private attribute.
    Confirms that size is type int and not a negative integer,else raise error.
    """

    def __init__(self, size=0):

        """check if size is an integer """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """check if size is not negative"""
        if size < 0:
            raise ValueError("size must be >= 0")

        """ private instance attribute named "size" """
        self.__size = size
