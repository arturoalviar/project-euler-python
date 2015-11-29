############################################################
#Problem 6
def sum_square_difference():
    '''Finds the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''
    #create an list from 1-100 and use the sum function to add up all the values in that array and then square it
    #use a map function to square each element in a list from 1-100 and then sum up all the values
    #subtract results
    return (sum([ x for x in range(1,101)]) ** 2) - (sum(map(lambda y : y ** 2, [ x for x in range(1,101)])))
