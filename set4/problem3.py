# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:04:56 2016

@author: ruialberto
"""

"""
Problem 3 - Valid Words 
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    lista = list()
    
    
    if word in wordList:
        var1 = True
    else:
        var1 = False
    
    novo_dic = getFrequencyDict(word)  
        
    for letra in word:
        if letra not in hand:
            break
        if hand[letra] >= novo_dic[letra]:
            lista.append(letra)
            
    
    lista = ''.join(lista)
    
     
    if word in lista:
        var2 = True
    else:
        var2 = False
        
    
    return (var1 and var2)
    