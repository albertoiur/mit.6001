# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:29:05 2016

@author: ruialberto
"""

"""
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl'.
"""

soma = 1
i=0
max = 0
s = 'azcbobobegghakl'
tamanho=len(s)
substr=''
temp_substr=''


for f in s:
    #print f
    if i==tamanho-1:
            break
    for j in s[i+1]:
       # print j
        
        if f <= j:
            soma = soma +1
            i = i + 1
            substr = substr + f + j
            if soma > max:
                max = soma
                temp_substr = substr
                
        else:
            soma=1
            substr=''
            i = i +1


if temp_substr=='':
    print ("Longest substring in alphabetical order is: ", s[0])
else:
    s2=temp_substr[0]
    s3=temp_substr[1:len(temp_substr)-1:2]  
    s4=temp_substr[-1]
    print ("Longest substring in alphabetical order is: ", s2+s3+s4)