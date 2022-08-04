l=['p',3,4,1,"A",6,'A','B',8,8,"c",9,"D","E", "E", "AA", "aa", "aa"]
l1=[]
for item in l:
    if item not in l1:
        l1.append(item)
for item in l1:
    if item in l:
        z=l.count(item)
        print(item,"=",z)