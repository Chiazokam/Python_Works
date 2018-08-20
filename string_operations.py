# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 00:21:28 2018

@author: CyberCloned
"""


def reverse(s):
    
    """This function takes a string and reverses the order"""
    
    str = ""
    for i in s:
        str = i + str
    return str


# =============================================================================
def mirror(s):
    """
    This function takes a string and outputs the string with
    its mirror image
    """ 
    str = ""
    for i in s:
        str = i + str
    return s + str
 
#rint(mirror("mother"))



# =============================================================================
def remove_letters(letter, string):
    """
    This function removes all the occurrences of letter 
    from the string and returns all other letters
    
    """
     
    new_string = ""
     
    for i in string:
         
        if i != letter:
            
            new_string += i
             
    return new_string
 
#print(remove_letters("i", "mississippi"))

# =============================================================================


def is_palindrome(string):
    
    string_reverse = reverse(string)
     
    if string == string_reverse:
            
        return True
       
    else:
            
       return False
        
#print(is_palindrome("straw warts"))

# =============================================================================

def count_a(text):
    count = 0
    for c in text:
        if c == "a":
            count += 1
    return(count)

#print(count_a("banana"))

#==============================================================================

def substring_count(substring, string):
    
    
    results = 0
    
    substring_len = len(substring)
    
    for i in range(len(string)):
        
        if substring[i:i+substring_len] == substring:
            
            string.remove(substring[i:i+substring_len])
            
            results += 1
            
    return results

print(substring_count("an", "banana"))