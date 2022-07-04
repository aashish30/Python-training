L1=['a',33,77,"ashish",'9','d',4]
L2=['d',0,'zx',4,22,"sw",166,33]

L3=[]
for item in L1:
    if item in L2:
        L3.append(item)
print(L3)