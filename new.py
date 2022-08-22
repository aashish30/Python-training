# l2 = ["one","two","three","four"]
# # str="_".join(l2)
# # print(str)
# l=[]
# for item in l2:
#     l.append(item)
#     l.append("_")
#
# l.pop()
# str="".join(l)
# print(str)
# l = [1,3,2,4,5,6]
# for i in range(len(l)-1, 0 ,-1 ):
#     print(l[i],end='')
# z=0
# s= "https://cisco.webex.com/meet/cisco123"
# for item in range(0,len(s)):
#     if s[item]=="/":
#         print(item)
# a="ashish"
# b="ashish"
# print(id(a))
# print(id(b))


# find the greatest among user input three value.

# print("enter 3 numbers")
# num1=int(input())
# num2=int(input())
# num3=int(input())
#
#
# max=num1
# if max<num2:
#     max=num2
# if max<num3:
#     max=num3
#
# print(max)






# d={"a":1,"b":2}
# d1={"c":3,"d":4}

# d2=d|d1
# print(d2)
#
# 10
# l=[]
# for x,y in d2.items():
#     l.append(x)
#     l.append(y)
# print(l)
# i=
# l=[1,4,7,19,36,105,8,223,445,75,499]
# while True:
#     if l[i]%2==1 :
#         print(i,"is odd")
#
#     elif l[i]//25:
#         break
#
#
#
#
#
#      l[i]//25==0

# l = ['potato', 'tomato', 'apple', 'kiwi', 'avocado','lichi', 'pear', 'pineapple']
# temp=''
# for item in l:
#     if len(item)>len(temp):
#         temp=item
#
# print("longest word is {}".format(temp))
# l1=[3,6,"b",4,"a"]
# l2=["x",2,3,"d",9]
# d={}
# for item in l1:
#     z=l1.index(item)
#     d[item]=l2[z]
# print(d)
# str = ["jump", "zoo", "zoo", "jump", "Taxi", "Aeroplane", "Taxi", "zoo"]
# l=[]
# for item in str:
#     if item not in l:
#         l.append(item)
#
# for item in l:
#     if item in str:
#         z=str.count(item)
#         print("no of",item,"is",z)

# str="ashish"
# x=str.split()
# print(x)
# s="".join(x)
# print(s)

# d1={}
# print("enter the number")
# i=int(input())
# for x in range(1,i+1):
#     d1[x]=x*x
# print(d1)
# d={"a":1,'b':2,"c":4}
# d1={}
# for x,y in d.items():
#     d1[y]=x
# print(d1)
# s="abcccccdeegg"
# d={}
# x=list(s)
# y=[]
#
# for item in x:
#     if item not in y:
#         y.append(item)
# print(y)
# for item in y:
#     if item in x:
#         d[item]=x.count(item)
# print(d)

s = 'Rockstar of the Galaxy'
x=s.split()
print(len(x[-1]))






