############################################################
#Problem 20


def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1)

def factorial_digit_sum():
    '''Finds the sum of the digits in the number 100!'''
    return sum(map(lambda x: int(x), str(factorial(100) ) ) )
