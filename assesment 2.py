# l=100
# def fun(n):
#
#     global l
#     l=l+10
#     print(l,n)
# fun(6)
# print(l)

# def fun(str1):
#     v=0
#     c=0
#     for item in str1:
#         if item=="a" or item=="e" or item=="i" or item=="o" or item=="u":
#             v+=1
#         else:
#             c+=1
#     print("vowels "+str(v)+"consnants "+str(c))
# fun("ashish")



# def fun():
#     l=["ashish", "india","usa"]
#     max_len=len(l[0])
#     max=l[0]
#     for i in l:
#         if (len(i)>max_len):
#             max_len=len(i)
#             max=i
#     print("max item is :{} and length of max item is :{}".format(max,max_len))
#
# fun()

# def fun(str1):
#     upper=0
#     lower=0
#     for i in str1:
#         if i.isupper():
#             upper+=1
#         elif i.islower():
#             lower+=1
#     print("upper case are" , upper,"lowercase are",lower)
#
# fun("My New Car")
import add_sub
print(add_sub.add(13,15))
print(add_sub.sub(45,3))




