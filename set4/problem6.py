# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:08:49 2016

@author: ruialberto
"""

"""
Problem 6 - Playing a Game
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    while True:
        valor = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if valor == 'n':
           n = HAND_SIZE
           palavra = dealHand(n)
           playHand(palavra, wordList, n)
        elif valor == 'e':
           break
        elif valor == 'r':
           try:
             playHand(palavra, wordList, n)
           except:
             print ('You have not played a hand yet. Please play a new hand first!')
        else:
            print ('Invalid command.')
