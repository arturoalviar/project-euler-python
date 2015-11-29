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
