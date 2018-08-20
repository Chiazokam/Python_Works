# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:44:31 2018

@author: CyberCloned
"""

def string_manip(string):
    
    """A function to remove the white spaces in a string and convert to a list."""
        
    string_to_list = string.split(" ")
        
    return string_to_list


def word_count(letter, new_list):
    
    """A function to count the number of words in a list that
    contain the letter specified"""
    
    count = 0
    
    for word in new_list:
        
        if letter in word:
            
            count += 1
            
    return count

    
def remove_punctuation(string):
    
    """A function to remove all punctuations from a string, call word_count 
    and string_manip on the string and return details about the string"""
    
    sans_punct = ""
    
    punctuation = "!\"#$%&’()*+,-./:;<=>?@[\\]^_‘{|}~"
    
    for char in string:
        
        if char not in punctuation:
            
            sans_punct += char
            
    wordlist = string_manip(sans_punct)
            
    e_words = word_count("e", wordlist)    
    
    list_len = len(wordlist)
    
    e_percent = (e_words/list_len) * 100
        
    return "Your text contains %d words of which %d (%d percent) contain an 'e'" %(list_len, e_words, e_percent)

 
fav_string = "But, wait a minute! I don't get all these gists about me getting married. I have personally called Nkiru and asked her to stop sharing all these unnecessary gists. They are not helpful."

print(remove_punctuation(fav_string))  