#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:23:15 2019

Nokia Test:
    
    -Found the percentage of 'bouncy' in a given interval
    -Bouncy is a number which has not sequentially increasing digits from 
    left to the right nor has decreassimg number from left to right

@author: luiz
"""


# Function to return thenumber for which the  interval [1, number] has the given percentage of bouncy numbers
def bouncy(percentage):
   # return round(sum(list(i) not in (sorted(i), sorted(i, reverse=True)) for i in map(str, range(1, n+1)))/n*100)
   num = 0
   i = 1
   actualPercentage = 0
   
   while actualPercentage < percentage:
      
       numStr = [int(d) for d in str(i)]
       if not ( numStr == sorted(numStr) or numStr == sorted(numStr, reverse=True)):
           num = num + 1
           actualPercentage = num*100/i
       i = i + 1
   return i     
   

def main1():
    print("Welcome to the solution of the Nokia Challenge")
    #get the number for 99% bouncy     
    print(bouncy(99))
        
if __name__ == '__main__':
    main1()
