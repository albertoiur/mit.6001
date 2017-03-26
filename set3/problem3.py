# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:49:46 2016

@author: ruialberto
"""

"""
Problem 3 - Printing Out all Available Letters

 implement the function getAvailableLetters that takes in one parameter - a list 
 of letters, lettersGuessed. This function returns a string that is comprised of
 lowercase English letters - all lowercase English letters that are not in 
 lettersGuessed.
 """
import string
 
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    temp = []
    abcedario = string.ascii_lowercase
    
    for i in abcedario:
        temp.append(i)
        
    for l in lettersGuessed:
        temp.remove(l)
        
    return ''.join(temp)