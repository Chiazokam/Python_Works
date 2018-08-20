# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:12:52 2018

@author: CyberCloned
"""

class Car:
    
    def __init__ (self, color, width, fly):
        
        self.color = "yellow"
        
        self.width = 20
        
        self.fly = True
        
    def change(self, color):
        
        self.color = color
        print("The color chosen here is", color)
        
    def jump(self, fly):
        
        self.fly = fly
        print("The fly feature of this car is", fly)
        
#benz = Car()

g = Car

Innoson = g("green", 50, "False")

print(Innoson.jump("True"))



