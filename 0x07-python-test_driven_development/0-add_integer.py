#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
<<<<<<< HEAD
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
=======
    """ Function that adds two integer and/or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
>>>>>>> ebd397515715c1fc4690ac26d88c262522df65b2
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
