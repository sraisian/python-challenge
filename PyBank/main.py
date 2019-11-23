# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 09:34:04 2019

@author: sarah
"""

import os
import csv
import pandas as pd
from pandas import DataFrame 


######PYBANK DATA##############
#read csv other way
#with open('C:/Users/sarah/Downloads/PyBank.csv') as file:
    #month=sum(1 for line in file)
#df = pd.read_csv (r'C:/Users/sarah/Downloads/PyBank.csv')

csvpath = os.path.join("PyBank.csv")
#read csv file to dataframe (df)
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    df = pd.read_csv(csvfile)



#sum up the Profit/Loss Column to get total profit
sum1 = df['Profit/Losses'].sum()
#count rows - header row to find total months
month = df['Profit/Losses'].count()

#create new col in df ("Difference") that is difference between P/L - P/L from prev
df['Difference'] = df['Profit/Losses'] - df['Profit/Losses'].shift(1)

#find average of the new 'Difference' col
average = df['Difference'].mean()
#only retrieve to two decimal places
average = round(average,2)

#find only instance where the difference equals max in 'Difference' col 
#to get corresponding date
maxrow = df[df['Difference']==df['Difference'].max()]

#find only instance where the difference equals min in 'Difference' col
#to get corresponding date
minrow = df[df['Difference']==df['Difference'].min()]
#print(minrow)
 
maxlist = []
for i in range((maxrow.shape[0])): 
#append to maxlist from maxrow result
    maxlist.append(list(maxrow.iloc[i, :]))   
#get first list within list
maxlist = maxlist[0]

minlist = []
for j in range((minrow.shape[0])): 
#append to maxlist from maxrow result
    minlist.append(list(minrow.iloc[j, :]))   
#get first list within list
minlist = minlist[0]

##### PRINT RESULTS ######
print("----------------------------")
print("Financial Analysis")
print("----------------------------")    
print("Total Months:" + str(month)) #-1 for the header row
print("Total Profit: $" + str(sum1))
print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + str(maxlist[0]) + " " + str(maxlist[-1]))
print("Greatest Decrease in Profits: "+ str(minlist[0]) + " " + str(minlist[-1]))

#create new txt file and write the above
f= open("Results.txt","w+")   

line1="Financial Analysis" + '\n'
line2 ="Total Months:" + str( month - 1) + '\n'
line3="Total Profit: $" + str(sum1) + '\n'
line4="Average Change: $" + str(average) + '\n'
line5="Greatest Increase in Profits: " + str(maxlist[0]) + " " + str(maxlist[-1]) + '\n'
line6="Greatest Decrease in Profits: "+ str(minlist[0]) + " " + str(minlist[-1]) + '\n'

f.writelines([line1, line2, line3, line4, line5, line6])

f.close()







