import fileinput
# def funcz():
#     with open('STORY.TXT','w') as fh:
#         ln =fh.readlines()
#         z=0
#         for i in ln:
#             if i[0]=="a":
#                 z+=1
#
#         print("lines",z)
#         fh.close()
#
# funcz()

# def Displaywords():
#
#     fh=open("STORY.TXT","r")
#     l=fh.read()
#     a=l.split()
#     for i in a:
#         if len(i)<4:
#             print(i)
#     fh.close()
#
# Displaywords()

# def Case():
#     z=0
#     fh=open("STORY.TXT","r")
#     l=fh.read()
#     a=l.split()
#     for i in a:
#         if i.islower():
#             z+=1
#
#     print("number of lowercase is",z)
# Case()

# def func(normal,*args,**kwargs):
#     print(normal)
#     for item in args:
#         print(item)
#     for key,values in kwargs.items():
#         print(f"{key} is a {values}")
#
# l=["a","b","c"]
# normal="i am normal"
# kw={"a":1,"b":2}
#
# func(normal,*l,**kw)


# def func(*args,**kwargs):
#     for item in args:
#         print(item)
#     for keys,values in kwargs.items():
#         print(f"{keys} is  {values}")
#
#
# l= [1,2,3,4,"a","b"]
# kw={"a":1,"b":2}
# func(*l,**kw)


str = """
QUEUE_NAME      PRIO STATUS          MAX JL/U JL/P JL/H NJOBS  PEND   RUN  SUSP
staf             70  Open:Active     500    -    -    -     0     0     0     0
dev              60  Open:Active     500    -    -    -     0     0     0     0
pos              55  Open:Active      50    -    -    -     0     0     0     0
"""

str = str.split('\n')
str.pop(0)
str.pop()
print(str)
name = input('Enter user name: ')
parameter = input('Enter the parameter to be checked: ')
k = str[0].split()
para_index = k.index(parameter)

for i in range(1,len(str)):
    j = str[i].split()
    for z in j:
        if z == name:
            print('\nUser Name: {} \n{}:{}'.format(name,parameter,j[para_index]))














