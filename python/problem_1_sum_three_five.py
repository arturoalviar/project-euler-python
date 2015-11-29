############################################################
#Problem one
def sum_three_five():
    '''Finds the sum of multiples of 3 and 5 below 1000'''
    #Use a lambda function to see if a value from 0 to 1000 is a multiple of 3 or 5.
    #Filter those values into a list and use sum to add up all the values
    return sum(filter(lambda x: x % 5 == 0 or x % 3 == 0, range(0,1000)))
