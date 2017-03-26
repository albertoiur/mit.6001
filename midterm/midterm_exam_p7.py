# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:30:16 2016

@author: ruialberto
"""


"""
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
 dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
"""
def f(a,b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    
    new_dic = {}
    new2_dic = {}
    lista = tuple()
    
    for item in d1:
        if item not in d2:
            new_dic[item]=d1[item]
            
    for item in d2:
        if item not in d1:
            new_dic[item] = d2[item]
            
    for i in d1:
        for j in d2:
            if i == j:
                new2_dic[i] = f(d1[i],d2[j])
                
    lista = (new2_dic, new_dic)         
    return lista   

   

### Teste ###
      
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
x = dict_interdiff(d1,d2)



        
            
            
         
    
    