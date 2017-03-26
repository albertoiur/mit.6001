# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:04:43 2016

@author: ruialberto
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    
    lista_tmp = []
    mono_inc = []
    mono_dec = []
    max = 0
        
    if len(L) < 2:
        return 0
    
    if len(L) == 2:
        if L[1] >= L[0] and lista_tmp == []:
            mono_inc.extend(L)
            return mono_inc
        else:
            mono_dec.extend(L)
            return mono_dec
            
            
    for i in range (len(L)-1):
        
        if L[i+1] >= L[i] and lista_tmp == []:
                       
            lista_tmp.append(L[i])
            lista_tmp.append(L[i+1])
            if i+2 == len(L):
                mono_inc.append(lista_tmp)
                break
            else:
                continue
            
                
        if L[i+1] >= L[i]:
            lista_tmp.append(L[i+1])
            if i+2 == len(L):
                mono_inc.append(lista_tmp)
                break
            else:
                continue
             
        else:
            mono_inc.append(lista_tmp)
            lista_tmp = []
            if i+2 == len(L):
                break
            
                
    for f in mono_inc:
        x = len(f)
        if x > max:
            resultado_inc = []
            resultado_inc.extend(f)
            max = x
            
                
                 
                    
    return resultado_inc


#print (longest_run([10,4,3,8,3,4,5,7,7,2,3,4]))
#print (longest_run([3,4])) 
#print (longest_run([8,3,4,5,7,7,7,8,2]))
#print (longest_run([4,1,2,3,4]))
#print (longest_run([2,3,1,4,6,8,9,3]))  
#print (longest_run([1,2,8,3,2,9,10,2]))  
#print (longest_run([1,2,3,3,4,2,7])) 
print (longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2] ))          