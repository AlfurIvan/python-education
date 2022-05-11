"""recursive factorial implementation"""


def recursive_factorial(n):
    """recursive factorial
    :arg n -- number, taken from user
    :return n if n == 1 -- start of calculation factorial
    :return n * recur_factorial(n - 1) -- calculation &
    & finally, result
    """
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)


if __name__ == '__main__':
    # take input
    num = int(input("Enter a number: "))
    # validate
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        print(f"The factorial of{num} is {recursive_factorial(num)}")
