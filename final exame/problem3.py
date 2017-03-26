# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:25:12 2016

@author: ruialberto
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    
    num = int (us_num)
    recebe_num = []
    resultado_final =''
    
    try:
        if num >=0 and num <= 10:
            return trans[us_num]
        elif 10 < num < 20:
            recebe_num.append(us_num[-1])
            resultado_final = resultado_final + 'shi ' + trans[recebe_num[0]]
            return resultado_final
        elif num >= 20 and num <= 99:
            for f in us_num:
                recebe_num.append(f)
            if recebe_num[1] == '0':
                resultado_final = resultado_final + trans[recebe_num[0]] + ' shi'
            else:
                resultado_final = resultado_final + trans[recebe_num[0]] + ' shi ' +  trans[recebe_num[1]]
            return resultado_final
    except ValueError:
        return 0
            
        
        
valor = convert_to_mandarin('30')   
print (valor)    
 
        
        
        
    
    
    