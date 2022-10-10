def squareroot(number):
    if number < 0:
        raise ValueError("Square root of negative number does not exist")
    else:
        return number**0.5