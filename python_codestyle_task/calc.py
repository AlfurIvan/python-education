"""This is primitive calculator"""


class Calculator:
    """
    This is a class of primitive calculator. You can use him by call one of methods
    """

    @classmethod
    def addition(cls, arg1, arg2):
        """
        Here the simple method which returns the sum of two numbers
        :param arg1: first operand to addition
        :param arg2: second operand to addition
        :return: the sum of :param a: and :param b:
        """
        return arg1 + arg2

    @classmethod
    def subtraction(cls, arg1, arg2):
        """
        Here the simple method which returns the difference of two numbers
        :param arg1: first operand to subtraction
        :param arg2: second operand to subtraction
        :return: the difference between :param a: and :param b:
        """
        return arg1 - arg2

    @classmethod
    def division(cls, arg1, arg2):
        """
        Here the simple method which returns the division of two numbers
        :param arg1: first operand to division
        :param arg2: second operand to division
        :return: the division :param a: on :param b:
        """
        return arg1 / arg2

    @classmethod
    def multiplication(cls, arg1, arg2):
        """
        Here the simple method which returns the multiplication of two numbers
        :param arg1: first operand to multiplication
        :param arg2: second operand to multiplication
        :return: the multiplication of :param a: and :param b:
        """
        return arg1 * arg2
