#Arturo Alviar
#Project Euler problems
############################################################
#Problem one
def sum_three_five():
    '''Finds the sum of multiples of 3 and 5 below 1000'''
    #Use a lambda function to see if a value from 0 to 1000 is a multiple of 3 or 5.
    #Filter those values into a list and use sum to add up all the values
    return sum(filter(lambda x: x % 5 == 0 or x % 3 == 0, range(0,1000)))

############################################################
#Problem 2

def even_fibo():
    '''Finds the sum of the even-valued terms'''
    a, b = 0, 1
    fibo_sum = 0
    limit = 300
    while limit > 0:
        a,b = b, b+a
        if a & 1 == 0:
            fibo_sum += a
        if a > 4000000:
            break
        limit -= 1
    return fibo_sum


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
            start+=2 #add two since %2 only works if number is even
    return start

############################################################
#Problem 6
def sum_square_difference():
    '''Finds the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''
    #create an list from 1-100 and use the sum function to add up all the values in that array and then square it
    #use a map function to square each element in a list from 1-100 and then sum up all the values
    #subtract results
    return (sum([ x for x in range(1,101)]) ** 2) - (sum(map(lambda y : y ** 2, [ x for x in range(1,101)])))

############################################################
#Problem 16

def power_digit_sum():
    '''Finds the sum of the digits of the number 2^1000?'''
    #Since every string is a list, we can map that using map and convert every index
    #value into a int and then sum it all up

    return sum(map(lambda x: int(x), str(2 << 999)))


############################################################
#Problem 20
def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)

def factorial_digit_sum():
    '''Finds the sum of the digits in the number 100!'''
    return sum(map(lambda x: int(x), str(factorial(100) ) ) )


############################################################
#Problem 25
def thousand_digit_fibo_num(index=0):
    '''Finds the index of the first term in the Fibonacci sequence to contain 1000 digits?'''
    a , b = 0 , 1
    limit = 100000
    while limit > 0:
        a , b = b , b + a
        index += 1
        if (len(str(a)) == 1000):
            break
        limit -= 1

    return index
