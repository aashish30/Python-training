with open('log.html','r') as fh:
    str1 = fh.read()
    # print(str1)
    str1 = str1.split('\n')
    print(str1)
    dict = {}
    first =  1
    last = 2
    for i in range(0,len(str1)//4):
        dict[str1[first]] = str1[last]
        first += 4
        last += 4
    print(dict)

