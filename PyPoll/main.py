# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:09:01 2019

@author: sarah
"""

import os
import csv
import pandas as pd
from pandas import DataFrame 

####PYPOLL DATA#########
#read csv file to dataframe (df) through home path
#df = pd.read_csv (r'C:/Users/sarah/Downloads/PyPoll.csv')
csvpath = os.path.join("PyPoll.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    df = pd.read_csv(csvfile)

#count unique values in Voter ID 
count1 = df['Voter ID'].nunique() 
#count unique voter id by candidate
candidatedf = df.groupby(['Candidate'],as_index=False).count()
print(candidatedf)

#retrieve total vote counts by each candidate
correytotal = candidatedf.iloc[0]['Voter ID']
khantotal = candidatedf.iloc[1]['Voter ID']
litotal = candidatedf.iloc[2]['Voter ID']
otooleytotal = candidatedf.iloc[3]['Voter ID']

#counting total votes, also compare to other sum to cross check
totalvotes = correytotal + khantotal + litotal + otooleytotal
#find percentage of total votes by each candidate
correypercent= round(correytotal/totalvotes * 100, 2)
khanpercent= round(khantotal/totalvotes * 100, 2)
lipercent= round(litotal/totalvotes * 100, 2)
otooleypercent= round(otooleytotal/totalvotes * 100, 2)

#find out which is the winner!
if correytotal > khantotal and litotal and otooleytotal:
    winner = "Correy"
    
if khantotal > correytotal and litotal and otooleytotal:
    winner = "Khan"
    
if litotal > khantotal and correytotal and otooleytotal:
    winner = "Li"
    
if otooleytotal > khantotal and litotal and correytotal:
    winner = "O'Tooley"


###########PRINT RESULTS################
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalvotes))
print("-------------------------")
print("Khan: " + str(khanpercent) + "% " + "(" + str(khantotal) + " votes" + ")")
print("Correy: " + str(correypercent) + "% " + "(" + str(correytotal) + " votes" + ")")
print("Li: "+ str(lipercent) + "% " + "(" + str(litotal) + " votes" + ")")
print("O'Tooley: " + str(otooleypercent) + "% " + "(" + str(otooleytotal) + " votes" + ")")
print("-------------------------")
print("Winner: " + winner + "!")
print("-------------------------")


f= open("Results.txt","w+")   

line1="Election Results" + '\n'
line2 ="Total Votes:" + str(totalvotes) + '\n'
line3= "Khan: " + str(khanpercent) + "% " + "(" + str(khantotal) + " votes" + ")" + '\n'
line4= "Correy: " + str(correypercent) + "% " + "(" + str(correytotal) + " votes" + ")" + '\n'
line5= "Li: "+ str(lipercent) + "% " + "(" + str(litotal) + " votes" + ")" + '\n'
line6= "O'Tooley: " + str(otooleypercent) + "% " + "(" + str(otooleytotal) + " votes" + ")" '\n'
line7= "And the winner is " + winner + "!"

f.writelines([line1, line2, line3, line4, line5, line6, line7])

f.close()

