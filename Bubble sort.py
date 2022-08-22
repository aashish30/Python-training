# l=[4,9,0,11,99,77,44,3,7]
# for i in range(len(l)):
#     for j in range(0,len(l)-i-1):
#         if l[j]>l[j+1]:
#             l[j] ,l[j+1]=l[j+1] ,l[j]
# print(l)


def fun1(l1):
    for item in l1:
        print(item, end=" ")


s='''Bus info Device Class Description
============================================================
pci@0000:1d:00.0 eno5 network VIC Ethernet NIC
pci@0000:1d:00.1 eno6 network VIC Ethernet NIC
pci@0000:3b:00.0 eno1 network Ethernet Controller 10G X550T
pci@0000:3b:00.1 eno2 network Ethernet Controller 10G X550T
pci@0000:5e:00.0 enp94s0f0 network Ethernet Controller XL710 for 40GbE QSFP+
pci@0000:5e:00.1 enp94s0f1 network Ethernet Controller XL710 for 40GbE QSFP+
pci@0000:5e:02.0 network Illegal Vendor ID
pci@0000:5e:02.1 network Illegal Vendor ID
pci@0000:5e:0a.0 enp94s10 network Illegal Vendor ID
pci@0000:5e:0a.1 enp94s10f1 network Illegal Vendor ID
pci@0000:d8:00.0 enp216s0f0 network Ethernet Controller XL710 for 40GbE QSFP+
pci@0000:d8:00.1 enp216s0f1 network Ethernet Controller XL710 for 40GbE QSFP+
pci@0000:d8:02.0 network Illegal Vendor ID
pci@0000:d8:02.1 network Illegal Vendor ID
pci@0000:d8:0a.0 enp216s10 network Illegal Vendor ID
pci@0000:d8:0a.1 enp216s10f1 network Illegal Vendor ID
vnet0 network Ethernet interface
vnet3 network Ethernet interface
virbr0-nic network Ethernet interface
kvm-monitoring network Ethernet interface
vnet2 network Ethernet interface
virbr0 network Ethernet interface
ex4000 network Ethernet interface
vnet1 network Ethernet interface'''

l=[]
x=s.split("\n")
x.pop(0)
x.pop(0)


for item in x:
    if item.__contains__("40GbE QSFP+"):
        a=item.split()
        l.append(a[1])
fun1(l)














