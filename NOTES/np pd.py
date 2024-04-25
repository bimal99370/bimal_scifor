# import numpy as np
# import pandas as pd
#
# df = pd.read_csv("C:/Users/bimal/OneDrive/Desktop/Octane.csv")
# df.head()
# # df['employed'].value_counts()
# # df['employed'].replace({'no': 0,'yes : 1'},inplace = true)
# # df['employed'].replace({})
# def facto(n):
#     fact = 1
#     for i in range(1, n+1):
#         print(i)
#         fact = fact*i
#     print("factorial of {} is {}".format(n, fact))
#
# facto(6)
# from functools import reduce
#
# print(reduce((lambda i,fact=1: fact*i), [i for i in rangde
# def  even(n):
#     c = 0
#     e = 0
#     for i in range (1,n+1):
#         if i%2==0:
#             c = c+1
#     print("the no of even no",c)
#
#         # else :
#         # e = e + 1
#         # print("the no of odd no", e)
# even(100)
# r = (lambda n: "even" if n % 2 == 0 else "odd")
# print(r(5))
# a = print(lambda n: "even" if n % 2 == 0 else "odd")
# print(a)
# a=(lambda c : c**3 )(3)
print((lambda c : c**3 )(3))