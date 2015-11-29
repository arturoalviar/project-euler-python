############################################################
#Problem 16

def power_digit_sum():
    '''Finds the sum of the digits of the number 2^1000?'''
    #Since every string is a list, we can map that using map and convert every index
    #value into a int and then sum it all up

    return sum(map(lambda x: int(x), str(2 << 999)))
