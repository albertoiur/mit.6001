# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:47:48 2016

@author: ruialberto
"""

"""
Problem 2 - Printing Out the User's Guess

Implement the function getGuessedWord that takes in two parameters - a string, 
secretWord, and a list of letters, lettersGuessed. This function returns a string 
that is comprised of letters and underscores, based on what letters in 
lettersGuessed are in secretWord.
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    strnew = ''    
    if secretWord == '':
        strnew = ' _ '
    
    for l in secretWord:
        if l not in lettersGuessed:
            strnew = strnew + ' _ '
        else:
            strnew = strnew + l
            
    return strnew  