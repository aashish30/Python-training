str='''Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/19  unassigned      YES NVRAM  administratively down down
Te0/0/20               200.1.1.1       YES manual up                    up
Te0/0/21               1.1.0.2         YES manual up                    up
Te0/0/21.1             unassigned      YES TFTP   deleted               down
Te1/3/0                unassigned      YES NVRAM  administratively down down
GigabitEthernet0       unassigned      YES TFTP   down                  down '''

x=str.split("\n")
d={}
x.pop(0)
print(x)
for item in x:
    a=item.split()
    # print(a)

    # print(a[0],a[-1])
    d[a[0]]=a[-1]
print(d)




# n=100
# for i in range(2,n+1):
#     for j in range(2,i-1):
#         if i%j==0:
#             print(i ,"is not prime")
#         else:
#             print()

