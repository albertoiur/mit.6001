# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:29:43 2016

@author: ruialberto
"""

def f(i):
    return i * 2
    
def g(i):
    return i > 5
    
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    lista_temp =[]
    for valor in range(len(L)):
        x = g(abs(f(L[valor])))
        if x == False:
            lista_temp.append(L[valor])
            
    for i in range(len(lista_temp)):
        L.remove(lista_temp[i])
        
    print ('Lista----- ', L)
    if L==[]:
        return -1
    else:
        return max(L)    


#### Teste #####

#L = [5.0, -7.0, 76667879798798989898]
L = [0, -10, 5, 6, -4]  

maximo = applyF_filterG(L, f, g)  
print (maximo) 
