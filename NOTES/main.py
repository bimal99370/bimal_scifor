# num = int(input("enter a no: "))
# print((lambda x: "even"if x % 2 == 0 else "odd")(num))
# def evenodd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
#
# print(evenodd(6))
# list1=[2,3,4,5,6,7,8]
# print((lambda x: "even"if x % 2 == 0 else "odd")(list1))
# print((lambda x: x**2)(5))
list1=[2,3,4,5,6,7,8]
# map(<func>,<iterator>)
res= map(lambda x: x**3,list1)
print(list(res))
print(list(res))

