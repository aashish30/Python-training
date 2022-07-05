import re
str="""
switch01,te0/1,2378748485,8474857587
switch02,te0/2,2378748486,5474857187
switch03,te0/3,3378748485,9474857587
switch04,te0/4,4378748486,15474857187
"""
sw=re.findall(r'switch\d\d',str)
int=re.findall(r'te\d\/\d',str)
otput_data=re.findall(r'(?<=te\d\/\d,)..........',str)
switch={}
x=0
l1=[]
for i in sw:
    switch[i]=int[x]
    x+=1
print(switch)
switch1={}
y=0
for j,k in switch.items():
    switch1[j]={}
    switch1[j][k]=otput_data[y]
    y+=1
print(switch1)








