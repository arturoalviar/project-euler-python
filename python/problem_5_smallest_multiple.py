############################################################
#Problem 5
#Helper 1
#check if number has 2-10 as a multiple


def smallest_multiple_to_ten(num):
    return (num % 2 == 0 and num % 3 == 0 and num % 4 ==0 and num % 5 == 0 and num % 6 == 0 and num % 7 ==0 and num % 8 ==0 and num % 9 == 0 and num % 10 == 0)


#Helper 2
#check if number has 11-20 as a multiple
def smallest_multiple_to_twenty(num):
    return (num % 11 == 0 and num % 12 == 0 and num % 13 ==0 and num % 14 == 0 and num % 15 == 0 and num % 16 ==0 and num % 17 ==0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0)


#main
def smallest_multiple():
    '''Finds the smallest positive number that is evenly divisible by all of the numbers from 1 to 20'''
    done = False
    start = 2520 #given value from the problem
    while not done:
        if (smallest_multiple_to_ten(start) and smallest_multiple_to_twenty(start)):
            done = True #break out of loop
        else:
            start += 2 #add two since %2 only works if number is even
    return start
