#to create dic in key value pair from 2 list
#l1=['a','b',"c"]
# l2=[1,2,3]
# d={}
# # for item in l1:
# #     z=l1.index(item)
# #     d[item]=l2[z]
# # print(d)
# d=dict(zip(l1,l2))
# print(d)

#common between 2 list
# l1=[3,6,'b',4,'a',9,'z','d']
# l2=['x',2,3,'d',9]
#
# # for item in l1:
# #     if item in l2:
# #         l3.append(item)
# # print(l3)
#
# s1=set(l1)
# s2=set(l2)
# if (s1 & s2):
#     print(s1 & s2)

# t=((1,2,3,4,5),[1,4,7,9],{'a':3,"z":9})
# x=list(t)
# print(x[1][2])

# d={"a":1,"b":2,"c":3,"d":4}
# d["e"]=5
# d.update(b=22)
#
# print(d)

# string questions
# s="today is monday"
# s1="11th july"
# # s2=s+" "+s1
# x=s.split()
# y=s1.split()
# print(y)
# for item in y:
#     x.append(item)
# print(x)
# str1=" ".join(x)
# print(str1)

# s="today is monday"
# s1="11th july"
# s2=s+" "+s1
# s3=s2.replace(" ","_")
# print(s3)

#print odd num, break if divisible by 25,if even continue
# l=[1,4,7,19,36,105,8,223,445,75,499]
# l1=[]
#
# for item in l:
#     if item//25:
#         break
#     elif item%2==0:
#         continue
#     elif item%2==1:
#         l1.append(item)
#
# print(l1)
#print index of "/"
# s="https://cisco.webex.com/meet/prebr"
# for i in range(0,len(s)):
#     if s[i]=="/":
#         print(i)
# x=list(s)
# z=x.count("/")
# print(z)
# x.index("/")



#print(z)


str= """Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/19  unassigned      YES NVRAM  administratively down down
Te0/0/20               200.1.1.1       YES manual up                    up
Te0/0/21               1.1.0.2         YES manual up                    up
Te0/0/21.1             unassigned      YES TFTP   deleted               down
Te1/3/0                unassigned      YES NVRAM  administratively down down
GigabitEthernet0       unassigned      YES TFTP   down                  down
"""
o = str.split('\n')
o.pop(0)
# print(o)

d = {}

for i in o[1:-1]:
    x = i.split()
    print(x[0], x[4])
    d[x[0]]=x[4]
print(d)
#print sorted dictionary with string
# str1 = ['aaa is 34', 'bbb is 30','ccc is 18','ddd is 33','eee is 31']
# d={}
# d1 = {}
# for item in str1:
#
#     d[item.split()[0]]=int(item.split()[2])
# print(d)
#
# for i in sorted(d,key=d.get):
#     d1[i] = d[i]
# print(d1)

# str = 'Rockstar of the Galaxy'
# x=str.split()
# z=len(x)-1
# print(len(x[z]))

# str = "abcccccdeegg"
# d={}
# z=0
# l=[]
# for item in str:
#     if item not in l:
#         l.append(item)
# for item in l:
#     d[item]=str.count(item)
# print(d)
#
# l1=[1,2,3,4,[9,8],5]
# l2=[]
# l2=l1
# print(l2)
# l2.append(7)
# print(l1)
# l2=l1.copy()
# print(l2)
# l2.append(5)
# print(l1)

# d={"a":1,"b":6,"c":6,"d":1,"e":8}
# #d1{1:2,6:2,8:1}
# d1={}
# x=list(d.values())
# print(x)
# for item in x:
#     d1[item]=x.count(item)
# print(d1)






















