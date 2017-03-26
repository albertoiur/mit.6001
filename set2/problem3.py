# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:41:19 2016

@author: ruialberto
"""

"""
Problem 3 - Using Bisection Search to Make the Program Faster
"""

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
intervalo_inf = balance / 12
intervalo_sup = (balance * (1 + monthlyInterestRate)**12) / 12.0
tentativa_valor_minimo = (intervalo_inf + intervalo_sup)/2
sobra = balance 
precisao = 0.1  

while (sobra >= precisao):

    tentativa_valor_minimo = (intervalo_inf + intervalo_sup)/2 #Bissecção
    mes = 0
    
    while mes < 12:

        novo_balance = sobra - tentativa_valor_minimo
        monthInterest = annualInterestRate/12*novo_balance
        sobra = novo_balance+monthInterest
        mes = mes + 1
            

    if (sobra < 0): 

        intervalo_sup = tentativa_valor_minimo      
        sobra = balance  

    elif (sobra > precisao): 
        intervalo_inf = tentativa_valor_minimo
        sobra = balance     
        
print ("Lowest Payment: ", round(tentativa_valor_minimo,2))

