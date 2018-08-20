# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 12:55:13 2018

@author: CyberCloned
"""


"""newList = ["Mother", "Father", "Brother", "Sister", "Aunty", "Uncle"]

for (m, n) in enumerate(newList):
    
    print("%s is in position %d on the list" %(n, m))"""
    
    
    
"""def double_stuff(a_list):
 
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    print(new_list)
    return new_list



double_stuff([2, 3, 5, 7, 12])"""

#Functions to list out all the prime numbers below a certain number

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	     return False
    return True


def primes_lessthan(n):

    result = []
    
    for i in range(2, n):
        
        if is_prime_number(i):
            
            result.append(i)
    
    print(result)
    
    return result

primes_lessthan(340)

