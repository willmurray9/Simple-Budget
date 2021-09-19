#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 23:29:24 2021

@author: willmurray
"""
import csv

with open('SABudget.csv', 'r') as infile:
    reader = csv.reader(infile)
    budget = {rows[0]:rows[1] for rows in reader}
    
for k,v in budget.items():
    budget[k] = float(v)
    
print('Current Breakdown\nWeek  Amount')
for i in budget:
    print('{}\t{}'.format(i, budget[i]))  

week = input('What week would you like to add to? ')
cost = float(input('How much did you spend today? '))    

if week in budget:
    budget[week] += cost
else:
    budget[week] = cost
 
print('\nUpdated Breakdown\nWeek  Amount')
for i in budget:
    print('{}\t{}'.format(i, budget[i]))    
    
with open('SABudget.csv', 'w') as outfile:
    w = csv.writer(outfile)
    w.writerows(budget.items())

