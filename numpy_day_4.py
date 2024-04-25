# -*- coding: utf-8 -*-
"""numpy day 4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1io-Z6jB4BVkBrKQ4D0kJ8QOqoQ_EwcCM
"""

#reshaping the array#

# reshape : pproduct of the desired(new) shape of array should be equal size of the array

#transpose : it will revverse the shape of the function if its two dimension
            # more than 2 dimension, we are going to use axis to shape the array

#swapaxes : it is used to reshape any two dimension of the array

#flatten : this will flatten the array to one dimension.
            #c - contiguous (row wise flattening or row major)
            #f - fortran (column wise flattening or column major)
#ravel :

import numpy as np

ary1 = np.random.randint(10,20,(4,5))

ary1

ary1.size

ary1.reshape(2,2,5) # this is not a permanent change thats why we have to save it in a variable to make the change permanent

#  RESIZE
ary1.resize(2,2,5)
# thsi is a permanent change that why we dont have to store it in a variable

ary1

ary1.resize(4,5)

ary1

# ary1.resize(2,3,5)
# this resize is not possible because there is insufficeant number of values(scalar) that we want to convert.

#there is a way using refcheck = false
#ary1.resize((2,3,5),refcheck = false)

a1 = np.random.randint(10,20,(4,5))
a1

a1.resize((5,5),refcheck=False)
a1

np.resize(a1,(6,5)) #slightly diffrent from above

"""TRANSPOSE"""

a1

a3 = a1.transpose()
a3

#also you can use like this
a3 = a3.T
a3

np1 = np.random.randint(100,200,(4,6))
np1

np1.swapaxes(1,0) #it can only transpose only 2nd dimension

ary3 = np.random.randint(100,200,(2,4,6))
ary3

ary3.flatten()

# there is a order on this

ary3.flatten(order = 'c') #deafult order to flatten  row wise

ary3.flatten(order = 'f') #this is on column basis

ary3.ravel() # this is an alternative of flatten,this is not a permanent change

"""FUNCTIONS

where()
round()
argmax()
argmin()
min
max
sum
mean
median
mode
copy()
view()

"""

#WFERE : NP.WHERE((condition),<true output>,<false output>)

a = 100
b = 50

np.where(a>b,a,b)

a = 100
b = 50
c = 200
np.where(a > b and a > c,a,np.where (b>c,b,c))

a if a > b and a > c else (b if b > c else c)

#round function

x = np.random.rand(5)
x

np.round(x,2)

np.trunc(x) #it will not consider the decimal part

y = [0.5,2.6,5.7,8.5]
np.trunc(y)

np.argmax(y) #it will give the maximum index

z = ['apple','NaN',np.NaN]
z

import pandas as pd

df2 = pd.DataFrame(z)
df2

df2.fillna("orange")

y

z = y.copy()
z

#IN COPY IF WE CHANGE ANY INSTANCES THEN IT IS NOT CHANGED IN ANOTHER ONE

#IN VIEW IF WE CHANGE ANY INSTANCES THEN IT IS CHANGED IN ANOTHER ONE

z1 = ary1.view()
z1

ary1[2][1] = 500
ary1

z1

# here it changes both in ary1 and z2

# manipulation of arrays
#insert
     axis = none
     axis = 0 (row wise)
     axis = 1 (column wise)
#delete
#append
#concatenate
#split

np.insert(ary1, 2, 999,axis = None)

np.insert(ary1,2,999,axis = 0)

np.insert(ary1,2,999,axis = 1)

np.insert(ary1,(2,4),999,axis = 0)

np.insert(ary1,(2,4),[100,200,300,400,500],axis = 0) #we have to provide same number of values to insert.

