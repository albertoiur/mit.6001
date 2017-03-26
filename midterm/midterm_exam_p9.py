# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:11:37 2016

@author: ruialberto
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    new_lista = []
    
    for elemento in aList:
        tipo = type(elemento)
        if tipo is list or tipo is tuple:
            for elemento2 in flatten(elemento):
                new_lista.append(elemento2)
        else:
            new_lista.append(elemento)
            
    return new_lista        
        
    

### Teste ###

#aLista = [1, [2,3,4], 'rui', 4.5]  
aLista = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
x = flatten(aLista) 
print (x)

     
        
    
    
        
        
        
    
    