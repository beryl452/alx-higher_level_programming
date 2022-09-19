#!/usr/bin/python3

"""Define Class Rectangle""" 

class Rectangle:
    """
	A class Rectangle that defines a rectangle

	Args:
            width (int): width
            height (int): height

	Functions:
  	    __init__(self, width, height)
	    width(self)
	    width(self, value)
	    height(self)
            height(self, value)
    """
    def __init__(self, width=0, height=0):
        """
            Initialize rectangles
            Args:
                width (int): width
                height (int): height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter sets width if value is int and > 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter sets height if value is int > 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
            self.__height = value

