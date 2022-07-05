l=['2378748485', '2378748486', '3378748485', '4378748486']
d2={'switch01': 'te0/1', 'switch02': 'te0/2', 'switch03': 'te0/3', 'switch04': 'te0/4'}
d={}
d4={}
# for i in range(0,len(l)):
#     for x,y in d2.items():
#         d3[x]=y,":",l[i]
#
# print(d3)
l1=list(d2.values())
print(l1)
print(l)
d2=list(d2)
print(d2)
for item in l1:
    z=l1.index(item)
    d[item]=l[z]

print(d)
for item in d2:
    for x in d.values():
        d3[item]=x
print(d3)








