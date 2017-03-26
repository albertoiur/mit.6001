# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:45:29 2016

@author: ruialberto
"""

"""
Problem 1 - Is the Word Guessed 

 First, implement the function isWordGuessed that takes in two parameters
 - a string, secretWord, and a list of letters, lettersGuessed. This function
 returns a boolean - True if secretWord has been guessed (ie, all the letters 
 of secretWord are in lettersGuessed) and False otherwise.
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if secretWord == '':
        return False
    
    for l in secretWord:
        if l not in lettersGuessed:
            return False
            
    return True
