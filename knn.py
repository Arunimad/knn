import csv
import random
import pandas as pd
import numpy as np


#with open('sample.csv','rb') as csvfile:
 #   lines = csv.reader(csvfile)
  #  for row in lines:
   #   print row



df = pd.read_csv('sample.csv')
colnames=['Day','Gender']
df = pd.read_csv('sample.csv', names=colnames, header=None)

df['Day']= np.random.randint(1,31, df.shape[0])
df['Gender']= np.random.randint(0,2, df.shape[0])



input = input("Enter no. btw 1-100")



day=df['Day'].values
gender=df['Gender'].values

print df 
print day
print gender
