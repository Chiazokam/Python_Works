# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:12:52 2018

@author: CyberCloned
"""

class Car:
    
    #Class Variable
    car_manufacturer = "Stevie Combs"
    
    #Also defines the instance variables
    def __init__ (self, color, width, fly):
        
        self.color = color
        
        self.width = width
        
        self.fly = fly
        
        print("This is the car class with color", self.color)
      
        #Also defines the instance variable, color
    def change(self, color):
        
        self.color = color
        print("The color chosen here is", self.color)
      
        #Also defines the instance variable, fly
    def jump(self, fly):
        
        self.fly = fly
        print("The fly feature of this car is", self.fly)
        
#benz = Car()

Innoson = Car("purple", 50, "False")

Benz = Car("burgundy", 25, "True")

#Innoson.jump("True")

print(Innoson.color, Innoson.car_manufacturer)

print(Benz.color, Benz.car_manufacturer)


