#!/usr/bin/python3
"""
Module 6-square.py
Provides an empty class Square that defines a square
"""


class Square:
    """
    Provides an empty class Square that defines a square

    Attribute :
        Size (private) of the square

    Returns :
        Current square area
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the square """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter of the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Set the value of the size only if it is a positive integer """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter of the position of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Setter of the position of the square """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Print the square """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0] + '#' * self.__size)
