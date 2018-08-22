# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 23:18:36 2018

@author: CyberCloned
"""

class Fish:
    
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        
        self.first_name = first_name
        
        self.last_name = last_name
        
        self.skeleton = skeleton
        
        self.eyelids = eyelids
        
    def swim(self):
        print("The fish can swim")
        
    def swim_backwards(self):
        print("The fish can swim backwards")

#==============================================================================
        
#Define a child class to the Fish class. Inherits all of Fish, no extras        
class Trout(Fish):
    
    pass

#==============================================================================
    
#Another child class to the Fish class. Inherits all of Fish and adds its own method
class Clownfish(Fish):
    
    def live_with_anemone(self):
        
        print("The clown fish is coexisting with sea anemone")
        
#==============================================================================
        
#Another child class to the Fish class. Class has methods that override 
#the parent class methods
        
class Shark(Fish):
    
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        
        self.first_name = first_name
        
        self.last_name = last_name
        
        self.skeleton = skeleton
        
        self.eyelids = eyelids
        
    def swim_backwards(self):
        
        print("The shark cannot swim backwards but can sink backwards")
        
#==============================================================================

terry = Trout("Terry")

casey = Clownfish("Casey")

sammy = Shark("Sammy")

#==============================================================================

terry.swim()

casey.live_with_anemone()

sammy.swim_backwards()

sammy.swim()