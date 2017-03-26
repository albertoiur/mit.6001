# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:52:04 2016

@author: ruialberto
"""

"""
Problem 4 - The Game

Implement the function hangman, which takes one parameter - the secretWord the 
user is to guess. This starts up an interactive game of Hangman between the user
 and the computer. Be sure you take advantage of the three helper functions, 
 isWordGuessed, getGuessedWord, and getAvailableLetters.
"""
import string

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

    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    num_letters_secretword = len(secretWord)
    conta = 0
    tentativas = 8
    guessl = ""
    wguess = ""
    rep = True
        
    print("Welcome to the game, Hangman!")    
    print ("I am thinking of a word that is ", num_letters_secretword, " letters long.")
    print ("-----------")
    while tentativas > 0:
        avletters= getAvailableLetters(wguess)
        print ("You have ", tentativas, " guesses left.")
        print ("Available letters: ", avletters)      
        guessl = input("Please guess a letter: ")
        guessl = guessl.lower()
                   
        while True:
              char = guessl.isalpha()
              if char == False:
                  print ("Wrong type!")
                  guessl = input("Please guess a letter: ")
                  guessl = guessl.lower()
                  
              else:    
                 rep = isWordGuessed(guessl,avletters)
                 if rep == False:
                    y = getGuessedWord(secretWord, wguess) 
                    print ("Oops! You've already guessed that letter:", y)
                    print ("-----------")
                    print ("You have ", tentativas, " guesses left.")
                    print ("Available letters: ", avletters ) 
                    guessl = input("Please guess a letter: ")
                    guessl = guessl.lower()
                                         
                 else:
                    break     
        
        wguess = wguess + guessl
          
        x = isWordGuessed(guessl,secretWord)
        w = getGuessedWord(secretWord, wguess)
        if w == secretWord:
            y = getGuessedWord(secretWord, wguess)
            print ("Good guess: ", y)
            print ("-----------")
            conta = len(secretWord) 
            break
        elif x == True:
            conta = conta + 1
            y = getGuessedWord(secretWord, wguess)
            print ("Good guess: ", y)
            print ("-----------")
            if conta == num_letters_secretword:
               tentativas = 0
        else:
             y = getGuessedWord(secretWord, wguess)
             print ("Oops! That letter is not in my word: ", y) 
             print ("-----------")
             tentativas = tentativas - 1
    
    
    if conta == num_letters_secretword:
       print ("Congratulations, you won!")
    else:            
      print ("")                
      print ("Sorry, you ran out of guesses. The word was ", secretWord)
      