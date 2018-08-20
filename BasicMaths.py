# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:17:24 2018

@author: CyberCloned
"""
import math

x = int(input("Enter number x: "))

y = int(input("Enter number y: "))

z = x ** y

log_num = math.log(x, 2)

print("x ** y =  %d" %(z))

print("Log(%d) = %d" %(x, log_num))