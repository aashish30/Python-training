import re
str="""
switch01,te0/1,2378748485,8474857587
switch02,te0/2,2378748486,5474857187
switch03,te0/3,3378748485,9474857587
switch04,te0/4,4378748486,15474857187
"""
s=re.findall(r'switch\d\d',str)
s1=re.findall(r'te\d\/\d',str)
s2=re.findall(r'(?<=te\d\/\d,)..........',str)
d1={}
x=0
l1=[]
for i in s:
    d1[i]=s1[x]
    x+=1
print(d1)
d2={}
y=0
for j,k in d1.items():
    d2[j]={}
    d2[j][k]=s2[y]
    y+=1
print(d2)








