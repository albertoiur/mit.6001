# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:44:18 2016

@author: ruialberto
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    guess = 0.0
    increment = 0.01
    
    while (base**guess) <= num:
        guess = guess + increment
        
    tipo = type(num)

    if tipo is int:
        return round(guess)
    elif tipo is float:
        return round(guess) - 1
    


### Teste ###    
x = closest_power(10, 550.0)    
print (x)
