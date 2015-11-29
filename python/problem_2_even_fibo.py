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
