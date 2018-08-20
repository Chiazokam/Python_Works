# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:17:22 2018

@author: CyberCloned
"""

def bisect_algo(item, testlist):
    
    first = 0
    
    last = len(testlist) - 1
    
    found = False
    
    while first <= last and not found:
        
        midpoint = (first + last)// 2
        
        if testlist[midpoint] == item:
            
            found = True
            
        else:
            
            if testlist[midpoint] > item:
                
                last = midpoint - 1
                
            else:
                
                first = midpoint + 1
                
    return found



newlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(bisect_algo(15, newlist))