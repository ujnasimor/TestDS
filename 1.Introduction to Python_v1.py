##########################################
#Basic commands
571+95
19*17
print(57+39)
print(19*17)
print("Statinfer")

#Division example
34/56

#Error
Print(600+900) #used Print() instead of print()
576-'96'

#LAB: Basic Commands
973*75
22/7

##########################################
#Assignment of variables
income=12000
income

x=20
x

y=30
z=x*y
z

del x #deletes the variable
x

name="Jack"
name

print(name)


#Is there a difference between output of name and print(name)?

book_name="Practical business analytics \n using SAS"
book_name

print(book_name)


##Variables are lost after restarting shell

##########################################
#Naming convention

1x=20 #Doesn't work

x1=20 #works
x1

x.1=20 #Doesn't work
x.1

x_1=20 #works
x_1


##Variable and Datatypes
x=89
x

y=2.98
y

#delete variables
del a


##########################################
#Type of Objects 

##Numbers
age=30
age

weight=102.88
weight

x=17
x**2 #Square of x

##Defining Strings 
name="Sheldon"
msg="Statinfer Data Science Classes"

name
msg

#Accessing strings
print(name[0])
print(name[1])

print(msg[0:9]) #This is as good as substring

len(msg) #length of string
print(msg[10:len(msg)])

#Displaying string multiple time
msg="Site under Construction"
msg*10
msg*50

#There is a difference between print and just displaying a variable
message="Data Science on R and Data Science on Python \n"
message*10
print(message*10)

#String Concatenation
msg1="Site under Construction "
msg2=msg1+"Go to home page \n"
print(msg2)
print(msg2*10)

#Similar to array, but all the elements need not be of sametype

#Creating a list
mylist1=['Sheldon','Tommy', 'Benny']


#Accessing list elements
mylist1[0] #Python indexing starts from 0
mylist1[1]
mylist1[2]

#Appending to a list
mylist2=['L.A','No 173', "CR108877"]

final_list=mylist1+mylist2
final_list

#Updating list elements
final_list[2]
final_list[2]='Sunny'
final_list

#Length of list
len(final_list)

#Deleting an element in list
del final_list[5]
final_list


#Tuples
my_tuple=('Mark','Male', 55)
my_tuple
my_tuple[1]
my_tuple[2]

my_tuple[0]*10

#Tuples vs Lists

#tuple can't be updated
my_list=['Sheldon','Tommy', 'Benny']
my_tuple=('Mark','M', 55)

mylist[2]='Sunny'
my_list

my_tuple[3]=40

####
import time
time.localtime()

list(range(15, 25))



#Dictionaries in Python
#The key value pairs

city={0:"LA", 1:"PA" , 2:"FL"}
city

#Accessing values 
city[0]
city[1]
city[2]

#Make sure that we give the right key index
names={1:"David", 6:"Bill", 9:"Jim"}
names
names[0] #Doesn't work, why?
names[1]
names[2]
names[6]
names[9]

#Key need not be a number always
edu={"David":"Bsc", "Bill":"Msc", "Jim":"Phd"}
edu

edu[0]
edu[1]
edu[David]
edu["David"]

#Updating values in dictionary 
edu
edu["David"]
edu["David"]="MSc"
edu["David"]
edu


#Updating keys in dictionary 
#Delete the key and value element first and then add new element

city={0:"LA", 1:"PA" , 2:"FL"}

#How to make 6 as "LA"

del city[0]
city

city[6]="LA"
city

#Looking at keys and values
city.keys()
city.values()

edu.keys()
edu.values()

##########################################
#Packages

log(10)
exp(5)
sqrt(256)

import math
math.log(10)
math.exp(5)
math.sqrt(256)

import math as mt
mt.log(10)
mt.exp(5)
mt.sqrt(256)

#numpy package

import numpy as np

income = np.array([9000, 8500, 9800, 12000, 7900, 6700, 10000])
print(income) 
print(income[0])

expenses=income*0.65
print(expenses)

savings=income-expenses
print(savings)


#pandas package
import pandas as pd
buyer_profile = pd.read_csv('D:\\Google Drive\\Training\\Datasets\\Buyers Profiles\\Train_data.csv')

print(buyer_profile)

buyer_profile.Age
buyer_profile.Gender

buyer_profile.Age[0]
buyer_profile.Age[0:10]

#Matplotlib

import matplotlib as mp
import numpy as np

X = np.random.normal(0,1,1000)
Y = np.random.normal(0,1,1000)

mp.pyplot.scatter(X,Y)

#Sklearn 
import sklearn as sk
import pandas as pd

air = pd.read_csv("D:\\Google Drive\\Training\\Datasets\\AirPassengers\\AirPassengers.csv")
air

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(air[["Promotion_Budget"]], air[["Passengers"]])

#Coefficients
print(lr.coef_)
print(lr.intercept_)

##########################################
#If-Then-Else statement
#Checks the condition is true or false and do operations accordingly 

#If Condition
age=60
if age<50:
    print("Group1")
print("Done with If")

age=40
if age<50:
    print("Group1")
print("Done with If")



##If else statement

age=60
if age<50:
    print("Group1")
else:
    print("Group2")
print("Done with If else")


#Multiple conditions in if 
#Use elif

marks=75

if(marks<30):
    print("fail")
elif(marks<60):
    print("Second Class")
elif(marks<80):
     print("First Class")
elif(marks<100):
     print("Distinction")
else:
    print("Error in Marks")
    

marks=20

if(marks<30):
    print("fail")
elif(marks<60):
    print("Second Class")
elif(marks<80):
     print("First Class")
elif(marks<100):
     print("Distinction")
else:
    print("Error in Marks")
    
    

#Nested if

x=45

if(x<50):
    print("Number is less than 50")
    if(x<40):
         print ("Number is less than 40")
         if(x<30):
             print("Number is less than 30")
         else:
             print("Number is greater than 30")
    else:
        print("Number is greater than 40")
else:
    print("Number is greater than 50")


x=35

if(x<50):
    print("Number is less than 50")
    if(x<40):
         print ("Number is less than 40")
         if(x<30):
             print("Number is less than 30")
         else:
             print("Number is greater than 30")
    else:
        print("Number is greater than 40")
else:
    print("Number is greater than 50")


##########################################
##For loop

#Example-1
my_num=1

for i in range(1,20):
    my_num=my_num+1
    print("my num value is", my_num)
    i=i+1

#Example-2
sumx = 0 
x=1

for x in range(1,20): 
     sumx = sumx + x
     print(sumx)

##The break statement 
#To stop execution of a loop
#Stopping the loop in midway

sumx = 0 
x=1

for x in range(1,200): 
     sumx = sumx + x
     if(sumx>500):
         break
     print(sumx)
     

