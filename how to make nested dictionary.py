l = ['2378748485','2378748486','3378748485','4378748486']
dic = {'switch01':'te0/1','switch02':'te0/2','switch03':'te0/3','switch04':'te0/4'}
z = 0

d1 = {}

for k,v in dic.items():
    d1[k] = {}
    d1[k][v] = l[z]
    z = z+1
print(d1)