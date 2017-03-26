# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:21:35 2016

@author: ruialberto
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    soma = 0
    valor = 0
    
    for i,j in zip(listA,listB):
        valor = i * j
        soma = soma + valor
        
    return soma 
    



#Teste
x=dotProduct([12,6,8], [4,5,6])    
print ("Resultado do produto = ", x) 


   
    
    
    
    
    
    
 