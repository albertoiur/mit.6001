# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:50:41 2016

@author: ruialberto
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    L.reverse()
    
    for item in L:
        item.reverse()
        
        
        
### Teste ###
L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)   

     
        
    
    
    