# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:06:14 2016

@author: ruialberto
"""

"""
Problem 4 - Hand Length 
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    conta = 0    
    
    for letra in hand:
        conta = conta + int(hand[letra])
        
    return conta
    