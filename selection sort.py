l=[1,5,2,6,-1,0]

for i in range(len(l)):
    min=i
    for j in range(i+1,len(l)):
        if l[j] < l[min]:
            min=j
            (l[i],l[min]) = (l[min] , l[i])
print(l)
