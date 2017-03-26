# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:38:17 2016

@author: ruialberto
"""

"""
Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.
"""

balance = 3329
annualInterestRate = 0.2
pagamento_mensal = 10
monthlyInterestRate = annualInterestRate /12
novobalanco = balance -10


while novobalanco > 0:
    pagamento_mensal = pagamento_mensal + 10  
    novobalanco = balance
    mes = 0
    
    while mes < 12 and novobalanco > 0:
        novobalanco = novobalanco - pagamento_mensal
        taxa = monthlyInterestRate * novobalanco
        novobalanco = novobalanco + taxa
        mes = mes + 1
    novobalanco = round(novobalanco,2)
    
print ("Lowest Payment: ", pagamento_mensal) 

