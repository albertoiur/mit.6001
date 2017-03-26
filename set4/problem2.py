# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:03:31 2016

@author: ruialberto
"""

"""
Problem 2 - Dealing with Hands
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    novo_dic = hand.copy()
    
    for letra in word:
        valor = novo_dic[letra]
        subvalor = valor - 1
        novo_dic[letra] = subvalor
        
    return novo_dic  
    
    