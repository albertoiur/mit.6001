# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:25:22 2016

@author: ruialberto
"""

"""
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl'.
"""

s2 = 'bob'
soma = 0
x = len(s2)
s = 'azcbobobegghakl'
for i in range(len(s)):
    temp = s[i:x]
    if temp == s2:
        soma = soma + 1
        x = x +1
    else:
        x = x + 1    
        
print ("Number of times bob occurs is: " + str(soma))