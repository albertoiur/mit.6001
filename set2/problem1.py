# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:34:26 2016

@author: ruialberto
"""

"""
Write a program to calculate the credit card balance after one year if a 
person only pays the minimum monthly payment required by the credit card 
company each month.

Problem 1:

Test Case 2:
	      balance = 484
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      Result Your Code Should Generate Below:
	      Remaining balance: 361.61
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for f in range (12):
    monthly_interest_rate = annualInterestRate / 12
    minimum_monthly_payment = monthlyPaymentRate * balance
    monthly_unpaid_balance = balance - minimum_monthly_payment
    balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance )
    #print ("Month " + str(f+1) + " Remaining balance: ", round(balance,2))
        
print ("Remaining balance: " ,round(balance,2))

