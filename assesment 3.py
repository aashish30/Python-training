# import fileinput
# f=open("example1.txt","w")
# f.write("this is my first file")
# f.close()
#
# with open("example1.txt","r") as firstfile, open("example2.txt","a")as secondfile:
#     for line in firstfile:
#         secondfile.write(line)

# l=['p',3,4,1,"A",6,'A','B',8,8,"c",9,"D","E", "E", "AA", "aa", "aa"]
# l1=[]
# for item in l:
#     if item not in l1:
#         l1.append(item)
# for item in l1:
#     if item in l:
#         z=l.count(item)
#         print(item,"=",z)

# #Compare the first and last name and print the uncommon alphabets in your name
# print("enter your first name")
# str1=str(input())
# print("enter your last name")
# str2=str(input())
# l=[]
#
# for item in str1:
#     if item not in str2:
#         l.append(item)
# for item in str2:
#     if item not in str1:
#         l.append(item)
# print(l)
# 2.2) Sort the below list in decending order
# l= [1,5,2,6,-1,0]
# for i in range(len(l)):
#     for j in range(0,len(l)-1):
#         if l[j] < l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# l=[ 1,"b","c","A","D",'Z','f',1,-1]
# # to work

# s="""Address         Age       MAC Address     Interface       Flags
# 10.192.1.212    00:02:22  bc4a.56f3.f7cc  Vlan1001
# 10.192.1.213    00:14:05  bc4a.56f3.f80c  Vlan1001
# 10.192.1.214    00:01:53  bc4a.56f3.f80c  Vlan1001
# 10.192.1.217    00:00:03  40a6.b736.4750  Vlan1001
# 10.192.1.218    00:00:25  40a6.b735.9a30  Vlan1001
# 10.192.1.219    00:08:49  40a6.b735.9b40  Vlan1001
# 10.192.1.220    00:17:24  40a6.b735.d0f0  Vlan1001
# 10.192.1.221    00:00:21  40a6.b735.d0f0  Vlan1001
# 10.192.1.222    00:14:26  40a6.b735.d598  Vlan1001
# 10.192.1.223    00:00:13  40a6.g736.1eb8  Vlan1001
# 10.192.1.227    00:02:37  e8eb.34d6.550c  Vlan1001
# 10.192.1.228    00:14:32  e8eb.34h6.550c  Vlan1001
# 10.192.1.230    00:10:16  e8eb.34d2.1cec  Vlan1001
# 10.192.1.231    00:05:05  e8eb.34d2.1cec  Vlan1001
# 10.192.1.232    00:00:01  e8eb.34d2.192C  Vlan1001
# 10.192.1.233    00:00:12  e8eb.34d6-294c  Vlan1001
# 10.192.1.234    00:02:02  e8eb.34d6.27ac  Vlan1001
# 10.192.1.235    00:06:58  e8eb.34d6:1fcc  Vlan1001
# 10.192.1.236    00:00:26  e8eb.34d6.1fcc  Vlan1001
# 10.192.1.237    00:04:16  e8eb.34D6.1f2c  Vlan1001
# 10.192.1.238    00:08:54  e8eb.34d6.2a2c  Vlan1001
# 192.168.111.0   00:05:17  689e.0b8c.890f  Ethernet1/61
# 192.168.111.2   00:05:17  689e.0b8c.890f  Ethernet1/62  """
#
#
# x=s.split("\n")
# print(x)
# x.pop(0)
# print(x)
# for item in x:
#     str=item.split()
#     z=str[2]
#     print(z)
#     a=z.split(".")
#     valid=True
#     for item in a:
#
#         if len(item)!=4:
#
#             valid=False
#         if valid==True:
#             for i in item:
#
#                 if i=="a" or i=="b"or i=="c" or i=="d" or i=="e"or i=="f" or i=='A'or i=='B'or i=='C'or i=='D'or i=="E"or i=="F"or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
#                     valid=True
#
#                 else:
#                     valid=False
#                     break
#     if valid==True:
#         print("mac valid")
#     else:
#         print("mac invalid")


#4) Store the below input in a file, read from the file to get the status and vlan id's, store output in dictionary with key as vlan id and status as value.
#ex - Vlan1 as id and status as down,

s="""Interface Secondary VLAN(Type) Status Reason
-------------------------------------------------------------------------------
Vlan1 -- down Administratively down
Vlan10 -- down VLAN/BD is down
Vlan139 -- up --
Vlan1001 -- up --
Vlan1101 -- down VLAN/BD is down
Vlan1102 -- down VLAN/BD is down
Vlan1103 -- down VLAN/BD is down
Vlan1104 -- down VLAN/BD is down
Vlan1105 -- down VLAN/BD is down
Vlan1111 -- down VLAN/BD is down
Vlan1112 -- down VLAN/BD is down
Vlan1122 -- down VLAN/BD is down
Vlan1132 -- down VLAN/BD is down
Vlan1201 -- down VLAN/BD is down
Vlan1202 -- down VLAN/BD is down
Vlan1203 -- down VLAN/BD is down
Vlan1204 -- down VLAN/BD is down
Vlan1205 -- down VLAN/BD is down
Vlan1211 -- down VLAN/BD is down
Vlan1212 -- down VLAN/BD is down
Vlan1222 -- down VLAN/BD is down
Vlan1232 -- down VLAN/BD is down
Vlan2352 -- down VLAN/BD does not exist
Vlan2353 -- down VLAN/BD does not exist
Vlan3522 -- up --
Vlan3960 -- up --
Vlan3961 -- up --
Vlan3962 -- up --
Vlan3963 -- up --
Vlan3964 -- up --"""

x=s.split("\n")
x.pop(0)
x.pop(0)
d={}
print(x)
for i in x:
    a=i.split(" ")
    d[a[0]]=a[2]
print(d)


#  # From the below input create a list of device names which has 40GbE QSFP+, pass the list to a function and print the elements of list.
# s='''Bus info Device Class Description
# ============================================================
# pci@0000:1d:00.0 eno5 network VIC Ethernet NIC
# pci@0000:1d:00.1 eno6 network VIC Ethernet NIC
# pci@0000:3b:00.0 eno1 network Ethernet Controller 10G X550T
# pci@0000:3b:00.1 eno2 network Ethernet Controller 10G X550T
# pci@0000:5e:00.0 enp94s0f0 network Ethernet Controller XL710 for 40GbE QSFP+
# pci@0000:5e:00.1 enp94s0f1 network Ethernet Controller XL710 for 40GbE QSFP+
# pci@0000:5e:02.0 network Illegal Vendor ID
# pci@0000:5e:02.1 network Illegal Vendor ID
# pci@0000:5e:0a.0 enp94s10 network Illegal Vendor ID
# pci@0000:5e:0a.1 enp94s10f1 network Illegal Vendor ID
# pci@0000:d8:00.0 enp216s0f0 network Ethernet Controller XL710 for 40GbE QSFP+
# pci@0000:d8:00.1 enp216s0f1 network Ethernet Controller XL710 for 40GbE QSFP+
# pci@0000:d8:02.0 network Illegal Vendor ID
# pci@0000:d8:02.1 network Illegal Vendor ID
# pci@0000:d8:0a.0 enp216s10 network Illegal Vendor ID
# pci@0000:d8:0a.1 enp216s10f1 network Illegal Vendor ID
# vnet0 network Ethernet interface
# vnet3 network Ethernet interface
# virbr0-nic network Ethernet interface
# kvm-monitoring network Ethernet interface
# vnet2 network Ethernet interface
# virbr0 network Ethernet interface
# ex4000 network Ethernet interface
# vnet1 network Ethernet interface'''
#
# l=[]
# x=s.split("\n")
# x.pop(0)
# x.pop(0)
#
#
# for item in x:
#     if item.__contains__("40GbE QSFP+"):
#         a=item.split()
#         l.append(a[1])
# fun1(l)
#
# # n = 25
# # for i in range(2,n):
# #     if n%i==0:
# #         break
# # else:
# #     print("Prime")
#
















