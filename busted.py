# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:32:17 2018

@author: CyberCloned
"""


"""def newFunction(digit, maxNum = True):
    
    if maxNum:
        
        print(digit)
        
newFunction(64, False)"""

def whileLoop(num):
    
    ini = 0
    
    while ini <= num:
        
        if ini == 0:
            
            print("You haven't been busted yet!")
            
        elif ini == 1:
            
            print("You just got busted %d time" %(ini))
             
        else: 
        
            print("You just got busted %d times" %(ini))
                  
        ini = ini + 1
        
whileLoop(1000)