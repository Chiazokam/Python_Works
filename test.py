# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:32:17 2018

@author: CyberCloned
"""


"""def newFunction(digit, maxNum = True):

    if maxNum:

        print(digit)

newFunction(64, False)"""
"""
def whileLoop(num):

    ini = 0

    while ini < num:

        if ini == 0:

            print("You haven't been busted yet!")

        elif ini == 1:

            print("You just got busted %d time" %(ini))

        else:

            print("You just got busted %d times" %(ini))

        ini = ini + 1

whileLoop(15)"""
"""
def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0, 15, -33]))"""

def anagram(a, b):
    if len(a) != len(b):
        return False
    else:
        counter = 0
        for letter in a:
            if letter in b:
                counter += 1
        if counter == len(b):
            return True
        else:
            return False

#print(anagram("earthy", "heart"))

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

    smallest_number = alist[0]

    return smallest_number

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
mergeSort(alist)
print(mergeSort(alist))
#==============================================================================
def largest_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(largest_num_in_list([1, 2, -8, 0, 15, 33]))
