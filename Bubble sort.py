l=[4,9,0,11,99,77,44,3,7]
for i in range(len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j] ,l[j+1]=l[j+1] ,l[j]
print(l)