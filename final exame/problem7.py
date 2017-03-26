# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:26:34 2016

@author: ruialberto
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE 
    
    def calculo(x):
        total = 0
        tamanho = len(L)-1
        
        for i in range(len(L)):
            total = total + L[i]*x**tamanho
            tamanho = tamanho - 1
        return total
    return calculo    
    
"""   
    def inner(x):
        res = 0
        n = len(L)-1
        for e in range(len(L)):
            res += L[e]*x**n
            n -= 1
        return res
    return inner
    
"""
    
    
    
    