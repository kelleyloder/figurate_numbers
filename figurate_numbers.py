#!/usr/bin/python
''' figurate_numbers by Rony Edde and Kelley Loder'''

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_triangular(n):
    
    i = 1
    while n > 0:
        n -= i
        if n == 0:
            return True
        
        i+= 1

    return False
      

def is_tetrahedral(n):
 
    i = 1
    while n > 0:
        if is_triangular(i):
            n -= i
            if n == 0:
                return True
        
        i+= 1

    return False
    

def is_square(n):
     
    i = 1
    while n > 0:
        n -= i
        if n == 0:
            return True
 
        i += 2

    return False
   

def is_square_pyramidal(n):
     
    i = 1
    while n > 0:
        if is_square(i):
            n -= i
            if n == 0:
                return True
        
        i+= 1

    return False


def is_pentagonal(n):
    
    for i in range(1, n+1):
        compare_value = i * (3 * i - 1) / 2

        if compare_value == n:
            return True
        
        elif compare_value > n:
            return False
       
    
def is_prime_oblong(n):
    ''' returns True if n has exactly 2 prime divisors.'''
    for i in range(1, n):
        if is_prime(i):
            remain = divmod(n, i)
        
            # check if division returns an integer
            if remain[1] == 0 and is_prime(remain[0]) \
                and remain[0] != i:
                return True

    return False


def is_pointy(n):
    '''returns True if n is a sum of 2 tetrahedral numbers.'''
    for i in range(1, n):
        
        #check if i in tetrahedral
        if is_tetrahedral(i):
            if is_tetrahedral(n-i) and (n-i) != i:
                return True

    return False


def main():
    limit = 100

    for i in range(1, limit + 1):
        output_str = '%d ' % i
        
        if is_prime(i):
            output_str += 'prime'
        else:
            output_str += 'composite'

        if is_triangular(i):
            output_str += ', triangular'
        else:
            output_str += ', not triangular'
        
        if is_tetrahedral(i):
            output_str += ', tetrahedral'
        else:
            output_str += ', not tetrahedral'
        
        if is_square(i):
            output_str += ', square'
        else:
            output_str += ', not square'
        
        if is_square_pyramidal(i):
            output_str += ', square_pyramidal'
        else:
            output_str += ', not square pyramidal'

        if is_pentagonal(i):
            output_str += ', pentagonal'
        else:
            output_str += ', not pentagonal'
      
        if is_prime_oblong(i):
            output_str += ', prime oblong'
        else:
            output_str += ', not prime oblong'

        if is_pointy(i):
            output_str += ', pointy'
        else:
            output_str += ', not pointy'

        print output_str
    

if (__name__ == '__main__'):
    main()
