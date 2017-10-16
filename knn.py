import csv
import random
import pandas as pd
import numpy as np
from math import sqrt


#with open('sample.csv','rb') as csvfile:
 #   lines = csv.reader(csvfile)
  #  for row in lines:
   #   print row



df = pd.read_csv('sample.csv')
colnames=['Day','Gender']
df = pd.read_csv('sample.csv', names=colnames, header=None)

df['Day']= np.random.randint(1,31, df.shape[0])
df['Gender']= np.random.randint(0,2, df.shape[0])


train_data=df[:int(0.7*10)]
test_data = df[int(0.7*10):]



print '\n\n\t\t  PREDICT GENDER FROM DOB  \n\n'



input = input("Enter BirthDate : \t \n")



train_date=train_data['Day'].values
train_gender=train_data['Gender'].values
test_date=test_data['Day'].values
test_gender=test_data['Gender'].values


print '\tRANDOMLY GENERATED DATASET \n'
print df 

print '\t TRAINING DATA \n'
print train_data

print '\t TESTING DATA \n '
print test_data

small = input
gender=0

for i in range(len(train_date)):
     euc_dis = sqrt(pow((input-train_date[i]),2))
     if euc_dis < small:
         small = euc_dis
         gender = train_gender[i]


if (gender == 0):
    req_gender = 'MALE'
else:
    req_gender = 'FEMALE'





print '\n\n RESULTS'
print '\n Gender Obtained \t', req_gender



gender_temp = 0
correctness =0

for j in range(len(test_date)):
        input = test_date[j]
        for i in range(len(train_date)):
               euc_dis = sqrt(pow((input-train_date[i]),2))
               if euc_dis < small:
                   small = euc_dis
                   gender_temp = train_gender[i]
        
        if(gender_temp == test_gender[j]):
             correctness +=1



accuracy = float(correctness)/len(test_data)*100

print '\n Accuracy   :' , accuracy

        
